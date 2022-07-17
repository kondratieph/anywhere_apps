from django.shortcuts import render, redirect, HttpResponse
from .models import ToDo
from .forms import ToDoForm
from django.contrib import messages
from django.utils.safestring import mark_safe
# Последнее - для messages

def index(request):
    todo_items = ToDo.objects.all()
    if request.method == 'POST':
        new_todo = ToDo(title = request.POST['title'])
        new_todo.save()
        redirect('todo:index')
    unchecked = todo_items.filter(status=False)
    checked = todo_items.filter(status=True)
    dated =  todo_items.exclude(status=True).filter(due_date__isnull=False)
    return render(request, 'to_do_list/index.html',
    {'todo_items': todo_items, 'unchecked': unchecked, 'checked': checked, 'dated': dated})


def add_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
        else:
            messages.error(request, 'Вы ничего не написали, так нельзя!')
            return redirect('todo:index')
    else:
        messages.error(request, 'Похоже, что-то случилось!')
        return render(request, 'todo:index')


def edit_todo(request, pk):
    todo = ToDo.objects.get(pk=pk)
    form = ToDoForm(request.POST or None, instance=todo)
    if request.method == 'POST':
        list_of_input_ids=request.POST.getlist('status')
        if form.is_valid():
            form.save()
            return redirect('todo:index')
        else:
            messages.error(request, mark_safe('Вы ничего не написали, так нельзя! Если так и задумано, <a href="/app/do/" class="text-decoration-none"><b>можете вернуться</b></a> назад!'))
    return render(request, 'to_do_list/edit.html', {'todo': todo, 'form': form})


def change_status(request, pk):
    todo_item = ToDo.objects.get(id=pk)
    if todo_item.status == False:
        todo_item.status = True
    else:
        todo_item.status = False
    todo_item.save()
    return redirect('todo:index')


def delete_todo(request, pk):
    todo_item = ToDo.objects.get(id=pk)
    todo_item.delete()
    return redirect('todo:index')


def test(request):
    todo_items = ToDo.objects.all()
    unchecked = todo_items.filter(status=False)
    checked = todo_items.filter(status=True)
    dated =  todo_items.filter(due_date__isnull=True)
    return render(request, 'to_do_list/test.html', {'todo_items': todo_items, 'unchecked': unchecked, 'checked': checked, 'dated': dated})


