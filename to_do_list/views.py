from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm
from django.contrib import messages

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
        title = request.POST['title']
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
        elif len(title) > 80:
            messages.error(request, 'Текст вашей задачи слишком длинный (максимум: 80 символов)!')
        else:
            messages.error(request, 'Вы ничего не написали!')
        return redirect('todo:index')
    else:
        form = ToDoForm()
    return render(request, 'to_do_list/index.html', {'form': form})


def edit_todo(request, pk):
    todo = ToDo.objects.get(pk=pk)
    form = ToDoForm(request.POST or None, instance=todo)
    if request.method == 'POST':
        title = request.POST['title']
        if form.is_valid():
            form.save()
            return redirect('todo:index')
        elif len(title) > 80:
            messages.error(request, 'Текст вашей задачи слишком длинный (максимум: 80 символов)!')
        else:
            messages.error(request, 'Вы ничего не написали!')

    else:
        form = ToDoForm()
    return render(request, 'to_do_list/edit.html', {'todo': todo, 'form': form})


def change_status(request, pk):
    todo_item = ToDo.objects.get(id=pk)
    if todo_item.status == False:
        todo_item.status = True
        todo_item.due_date = None
    else:
        todo_item.status = False
    todo_item.save()
    return redirect('todo:index')


def delete_todo(request, pk):
    todo_item = ToDo.objects.get(id=pk)
    todo_item.delete()
    return redirect('todo:index')