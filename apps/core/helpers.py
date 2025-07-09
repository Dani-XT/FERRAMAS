from apps.utils.models import Region, Provincia, Comuna

def get_all_comunas():
    return Comuna.objects.all()

def get_all_provincias():
    return Provincia.objects.all()

def get_all_regiones():
    return Region.objects.all()

def get_comuna(pk):
    return Comuna.objects.get(pk=pk)

def get_provincia(pk):
    return Provincia.objects.get(pk=pk)

def get_region(pk):
    return Region.objects.get(pk=pk)