from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


class BaseCRUDView(View):
    """
    Base class for CRUD operations. 
    Basis für die CRUD-Operationen. Erweiterung der generischen CBV von Django um HTMX Funktionalitäten
    abbilden zu können.       
    """

    table_template = None
    row_template = None
    modal_template = None
    search_fields = ()
    ordering = ()

    def is_htmx(self, request):
        return request.headers.get('HX-Request') == 'true'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context


class HtmxCrudMixin:
    """
    Basis-Mixin für HTMX-gestützte CRUD-Views mit Template-Partials.
    Unterklassen setzen: model, form_class, template_name,
    partial_row, partial_add_form, partial_edit_form,
    list_url_name, queryset_order_by
    """
    model = None
    form_class = None
    template_name = None        # z.B. 'orga/koerperschaftstypen/kt_uebersicht.html'
    partial_row = None          # z.B. 'koerperschaftstypen_row'
    partial_add = None     # z.B. 'koerperschaftstypen_add_form'
    partial_edit = None
    partial_delete = None
    list_url_name = None        # für non-HTMX Redirect
    queryset_order_by = None
    context_object_name = 'object'   # Name im Template-Kontext

    session_filter_fields = {}
    # Mapping: Modell-Feldname → Session-Key
    # z.B. {'gemeinde_id': 'aktive_gemeinde', 'haushaltsjahr': 'aktives_hhjahr'}

    def get_queryset(self, request=None):
        qs = self.model.objects.all()

        if request and self.session_filter_fields:
            for field, session_key in self.session_filter_fields.items():
                value = request.session.get(session_key)
                if value:
                    qs = qs.filter(**{field: value})

        if self.queryset_order_by:
            qs = qs.order_by(self.queryset_order_by)

        return qs

    def _is_htmx(self, request):
        return request.headers.get('HX-Request') 

    def _partial(self, request, partial, context):
        return render(request, f'{self.template_name}#{partial}', context)


class ListView(HtmxCrudMixin, View):    
    def get(self, request):

        if self.order_by:
            print("Ordering queryset by:", self.order_by)  # Debug-Ausgabe der Sortierung
            try:
                context = {'values': self.get_queryset(request).order_by(self.order_by)}
                print("Context with ordering:", context)  # Debug-Ausgabe des Kontextes mit Sortierung
            except:
                context = {'values': self.get_queryset(request)}
                print("Error in ordering. Context without ordering:", context)  # Debug-Ausgabe bei Fehler in Sortierung
        else:
            context = { 'values': self.get_queryset(request)}


        if self.title:
            context['title'] = self.title

        return render(request, self.template_name, context)


class CreateView(HtmxCrudMixin, View):
    def get(self, request):
        form = self.form_class()
        return self._partial(request, self.partial_add, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print("Form data:", request.POST)  # Debug-Ausgabe der Formulardaten

        if form.is_valid():
            print("Form is valid. Cleaned data:", form.cleaned_data)  # Debug-Ausgabe der bereinigten Daten
            obj = form.save()
            print("Object created:", obj)  # Debug-Ausgabe des erstellten Objekts
            if self._is_htmx(request):
                #print("HTMX request detected. Returning partial.")  # Debug-Ausgabe für HTMX-Erkennung
                #print(self.partial_row)
                #print({self.context_object_name: obj})
                #print(self._partial(request, self.partial_row,
                #                     {'row': obj}))
                return self._partial(request, self.partial_row,
                                     {'row': obj})
            return redirect(self.list_url_name)
        # Formular mit Fehlern zurückgeben
        return self._partial(request, self.partial_add, {'form': form})


class UpdateView(HtmxCrudMixin, View):
    def get(self, request, id):
        print("GET request for UpdateView with id:", id)  # Debug-Ausgabe der ID
        obj = get_object_or_404(self.model, pk=id)
        print("Object to edit:", obj)  # Debug-Ausgabe des zu bearbeitenden Objekts
        form = self.form_class(instance=obj)
        print("Form for editing:", form)  # Debug-Ausgabe des Formulars
        return self._partial(request, self.partial_edit,
                             {self.context_object_name: obj, 'form': form})

    def post(self, request, id):
        obj = get_object_or_404(self.model, pk=id)
        form = self.form_class(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            if self._is_htmx(request):
                return self._partial(request, self.partial_row,
                                     {'row': obj})
            return redirect(self.list_url_name)
        return self._partial(request, self.partial_edit,
                             {'row': obj, 'form': form})


class DeleteView(HtmxCrudMixin, View):
    def get(self, request, id):
        obj = get_object_or_404(self.model, pk=id)
        return self._partial(request, 'delete_confirmation',
                             {'row': obj, 'titlesingular': self.titlesingular})

    def post(self, request, id):
        obj = get_object_or_404(self.model, pk=id)
        name = str(obj)
        obj.delete()
        if self._is_htmx(request):
            return HttpResponse('')   # leeres Element – HTMX entfernt die Row
        return redirect(self.list_url_name)


class CancelView(HtmxCrudMixin, View):
    def get(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        return self._partial(request, self.partial_row,
                             {self.context_object_name: obj})

















































"""
class CRUDListView(BaseCRUDView, ListView):
   
    # ListView für die Anzeige der Daten in einer Tabelle. 
    # Erweiterung um HTMX Funktionalitäten für die dynamische Aktualisierung der Tabelle.
   

    def get(self, request, *args, **kwargs):

        if self.is_htmx(request):
            # Wenn es sich um eine HTMX-Anfrage handelt, rendere nur die Zeilen der Tabelle
            return render(request, self.row_template, self.get_context_data())
        else:
            # Ansonsten rendere die gesamte Seite mit der Tabelle
            return render(request, self.table_template, self.get_context_data())
        
    
class CRUDCreateView(BaseCRUDView, CreateView):
   
    # CreateView für die Erstellung neuer Einträge. 
    # Erweiterung um HTMX Funktionalitäten für die dynamische Aktualisierung der Tabelle nach der Erstellung eines neuen Eintrags.
   

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.is_htmx(self.request):
            # Wenn es sich um eine HTMX-Anfrage handelt, rendere die Zeilen der Tabelle neu
            return render(self.request, self.row_template, self.get_context_data())
        else:
            # Ansonsten leite zur Liste weiter
            return response
    
class CRUDUpdateView(BaseCRUDView, UpdateView):
    
    #UpdateView für die Bearbeitung bestehender Einträge. 
    # Erweiterung um HTMX Funktionalitäten für die dynamische Aktualisierung der Tabelle nach der Bearbeitung eines Eintrags.
    

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.is_htmx(self.request):
            # Wenn es sich um eine HTMX-Anfrage handelt, rendere die Zeilen der Tabelle neu
            return render(self.request, self.row_template, self.get_context_data())
        else:
            # Ansonsten leite zur Liste weiter
            return response

class CRUDDeleteView(BaseCRUDView, DeleteView):
    
    #DeleteView für die Löschung bestehender Einträge. 
    # Erweiterung um HTMX Funktionalitäten für die dynamische Aktualisierung der Tabelle nach der Löschung eines Eintrags.
    

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if self.is_htmx(request):
            # Wenn es sich um eine HTMX-Anfrage handelt, rendere die Zeilen der Tabelle neu
            return render(request, self.row_template, self.get_context_data())
        else:
            # Ansonsten leite zur Liste weiter
            return response
"""
