from django.db import models

# Create your models here.
class Usuarios(models.Model):
    usrid = models.AutoField(auto_created=True, primary_key=True)
    usrsts = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    usrdate = models.DateTimeField(auto_now_add=True)
    usrdatemod = models.DateTimeField()
    xusrtype = [(0,'InActivo'),(1,'Clientes'),(2,'Usuario'),(13,'Viajero'),(69,'Administrador')]
    usrtype = models.PositiveSmallIntegerField(choices=xusrtype, default=1, verbose_name="Tipo Usuario") 
    usrnames = models.CharField(max_length=40, null=True, blank=True, verbose_name="Nombres")
    usrape01 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Apellido Paterno")
    usrape02 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Apellido Materno")
    xgenero = [('M','Masculino'),('F','Femenino'),('G','Generico')]
    usrgen = models.CharField(max_length=1, choices=xgenero, default='G', verbose_name="Genero")
    usrtel01 = models.BigIntegerField(null=False, blank=False, default=0, verbose_name="Telefono Principal")
    usrtel02 = models.BigIntegerField(null=False, blank=False, default=0, verbose_name="Telefono Secundario")

    def NombreCompleto(self):
        if self.usrape01 and self.usrape02:
            xureg = "{0} {1}, {2}"
            return xureg.format(self.usrape01, self.usrape02, self.usrnames).upper().strip()
        else:
            xureg = "{0}, {1}"
            return xureg.format(self.usrape01, self.usrnames).upper().strip()

    def NombreCodigo(self):
        xureg = "{0} :: {1}"
        return xureg.format(self.usrid, self.kNombreCompleto()).upper().strip()

    def Courier(self):
        if self.usrtype == 13 or self.usrtype == 69:
            xureg = "{0}"
            return xureg.format(self.kNombreCompleto()).upper().strip()

    def __str__(self):
        xureg = "{0}"
        return xureg.format(self.kNombreCodigo()).upper().strip()


class TipoDocumento(models.Model):
    tdid = models.AutoField(auto_created=True, primary_key=True)
    tdsts = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    tddate = models.DateTimeField(auto_now_add=True)
    tddatemod = models.DateTimeField()
    tddes = models.CharField(max_length=40, null=True, blank=True, verbose_name="Tipo Documento")

    def __str__(self):
        xureg = "{0} :: {1}"
        return xureg.format(self.tdid, self.tddes).upper().strip()

class UsuarioDocumento(models.Model):
    udid = models.AutoField(auto_created=True, primary_key=True)
    udsts = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    uddate = models.DateTimeField(auto_now_add=True)
    uddatemod = models.DateTimeField()
    udusrcode = models.ForeignKey(Usuarios, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Codigo Usuario")
    udtdid = models.ForeignKey(TipoDocumento, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Tipo Documento")
    udnum = models.CharField(max_length=40, null=True, blank=True, verbose_name="Numero Documento")

    def __str__(self):
        xudreg = "{0} :: {1} :: {2}"
        return xudreg.format(self.udtdid, self.udnum, self.udusrcode.kNombreCompleto()).upper().strip()

class AeroLinea(models.Model):
    alid = models.AutoField(auto_created=True, primary_key=True)
    alsts = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    aldate = models.DateTimeField(auto_now_add=True)
    aldatemod = models.DateTimeField()
    alusrcode = models.ForeignKey(Usuarios, null=False, blank=False, on_delete=models.CASCADE)
    alcode = models.CharField(max_length=20, null=True, blank=True, verbose_name="AeroLinea Codigo")
    alstatus = models.CharField(max_length=30, null=True, blank=True, verbose_name="AeroLinea Status")
    aldes = models.CharField(max_length=30, null=True, blank=True, verbose_name="AeroLinea Nombre")

    def SkyMiles(self):
        xureg = "{0} :: {1}"
        return xureg.format(self.alcode, self.alusrcode.kCourier()).upper().strip()

    def __str__(self):
        xureg = "{0} :: {1}"
        return xureg.format(self.aldes, self.SkyMiles()).upper().strip()
    
class UsuarioVuelo(models.Model):
    ufid = models.AutoField(auto_created=True, primary_key=True)
    ufsts = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    ufdate = models.DateTimeField(auto_now_add=True)
    ufdatemod = models.DateTimeField()
    ufalcode = models.ForeignKey(AeroLinea, null=False, blank=False, on_delete=models.CASCADE)
    ufsrc = models.PositiveSmallIntegerField(null=False, blank=False, default=1, verbose_name="Vuelo Origen")
    ufreserva = models.CharField(max_length=10, null=True, blank=True, verbose_name="Reserva Numero")
    ufdatefly = models.DateField(null=False, blank=False, verbose_name="Reserva Fecha")
    uftimefly = models.TimeField(null=False, blank=False, verbose_name="Reserva Hora")
    ufnumb = models.CharField(max_length=10, null=True, blank=True, verbose_name="Vuelo Numero")
    ufseat = models.CharField(max_length=10, null=True, blank=True, verbose_name="Asiento")
    ufbags = models.PositiveSmallIntegerField(null=False, blank=False, default=1, verbose_name="Maletas")

    def __str__(self):
        xureg = "Courier: {0} / Rewserva: {1} :: Vuelo: {2} :: Asiento: {3} :: Maletas: {4}"
        return xureg.format(self.ufalcode.SkyMiles(), self.ufreserva, self.ufnumb, self.ufseat, self.ufbags).upper().strip()
	
class Direccion(models.Model):
    addid = models.AutoField(auto_created=True, primary_key=True)
    addsts = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    adddate = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    adddatemod = models.DateTimeField()
    addusrcode = models.ForeignKey(Usuarios, null=False, blank=False, on_delete=models.CASCADE, verbose_name="User Code")
    addadd = models.CharField(max_length=50, null=True, blank=True, verbose_name="Address")
    addcity = models.CharField(max_length=30, null=True, blank=True, verbose_name="City")
    addzipcode = models.CharField(max_length=20, null=True, blank=True, verbose_name="ZipCode")
    addstate = models.CharField(max_length=30, null=True, blank=True, verbose_name="State")
    addcountry = models.CharField(max_length=50, null=True, blank=True, verbose_name="Country")
	
class Empresa(models.Model):
    empid = models.AutoField(auto_created=True, primary_key=True)
    empsts = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    empdate = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    empdatemod = models.DateTimeField()
    empname = models.CharField(max_length=100, null=True, blank=True, verbose_name="Empresa Name")
    empusrcode = models.ForeignKey(Usuarios, null=False, blank=False, on_delete=models.CASCADE, verbose_name="User Code")
    
class Agencia(models.Model):
    ageid = models.AutoField(auto_created=True, primary_key=True)
    agests = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    agedate = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    agedatemod = models.DateTimeField()
    agename = models.CharField(max_length=20, null=True, blank=True, verbose_name="Empresa Name")
    ageempid = models.ForeignKey(Empresa, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Empresa Code")
    ageusrcode = models.ForeignKey(Usuarios, null=False, blank=False, on_delete=models.CASCADE, verbose_name="User Code")
    
class Rastreo(models.Model):
    trkid = models.AutoField(auto_created=True, primary_key=True)
    trksts = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    trkdate = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    trkdatemod = models.DateTimeField()
    trkname = models.CharField(max_length=100, null=True, blank=True, verbose_name="TrkName")
    
class PaqueteEncabezado(models.Model):
    pkhid = models.AutoField(auto_created=True, primary_key=True)
    pkhsts = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    pkhdate = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    pkhdatemod = models.DateTimeField()
    pkhcode = models.IntegerField(null=False, blank=False, unique=False, verbose_name="PkgCode")
    pkhempid = models.PositiveSmallIntegerField(null=False, blank=False)
    pkhsrcusrcode = models.IntegerField(null=False, blank=False, verbose_name="SrcUsrCode")
    pkhdstusrcode = models.IntegerField(null=False, blank=False, verbose_name="DstUsrCode")
    pkhpeso = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    pkhmonto = models.DecimalField(max_digits = 10, decimal_places = 2, null=False, blank=False, default=0)
    
class PaqueteDetalle(models.Model):
    pkdid = models.AutoField(auto_created=True, primary_key=True)
    pkdsts = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    pkddate = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    pkddatemod = models.DateTimeField()
    pkdcode = models.IntegerField(null=False, blank=False, unique=False, verbose_name="PkgCode")
    pkdempid = models.PositiveSmallIntegerField(null=False, blank=False)
    pkdsrcusrcode = models.IntegerField(null=False, blank=False, verbose_name="SrcUsrCode")
    pkddstusrcode = models.IntegerField(null=False, blank=False, verbose_name="DstUsrCode")
    pkdpeso = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    pkdmonto = models.DecimalField(max_digits = 10, decimal_places = 2, null=False, blank=False, default=0)
    
