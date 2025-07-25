from django.shortcuts import render, redirect
from . import dbcon  # MongoDB connection

# Show the Add Form
def add(request):
    return render(request,'add.html')

# Save New Intern Record
def addsave(request):
    if request.method == 'POST':
        regno = request.POST.get('regno', '')
        name = request.POST.get('name', '')
        department = request.POST.get('department', '')
        company = request.POST.get('company', '')
        duration = request.POST.get('duration', '')
        domain = request.POST.get('domain', '')
        mail = request.POST.get('mail', '')

        data = {
            "regno": regno,
            "name": name,
            "department": department,
            "company": company,
            "duration": duration,
            "domain": domain,
            "mail": mail
        }
        dbcon.col.insert_one(data)
        return redirect('listdata')
    else:
        return redirect('add')  # redirect to form if GET request

# List All Intern Records
def listdata(request):
    interns = dbcon.col.find()
    return render(request, 'list.html',{'var': interns})

# Edit an Intern Record
def edit(request, regno):
    entry = dbcon.col.find_one({"regno": regno})
    if request.method == "POST":
        name = request.POST.get("name", "")
        department = request.POST.get("department", "")
        company = request.POST.get("company", "")
        duration = request.POST.get("duration", "")
        domain = request.POST.get("domain", "")
        mail = request.POST.get("mail", "")

        dbcon.col.update_one(
            {"regno": regno},
            {"$set": {
                "name": name,
                "department": department,
                "company": company,
                "duration": duration,
                "domain": domain,
                "mail": mail
            }}
        )
        return redirect('listdata')
    return render(request,"edit.html",{"entry": entry})

# Delete an Intern Record
def delete(request, regno):
    dbcon.col.delete_one({"regno": regno})
    return redirect("listdata")



# Create your views here.
