# Analisis_Publisher


![AD Manager](https://user-images.githubusercontent.com/110134592/267164313-1a9fab99-8cd9-4a10-b65e-8d8a9d23ca3f.jpg) 
![Looker](https://user-images.githubusercontent.com/110134592/267165962-7e81d466-1159-4b20-9a81-a5aa470a1fe9.png)

Este proyecto surge luego de hacer una pasantía en una empresa que se dedicaba a optimizar las subastas programáticas de sus clientes. La subasta de anuncios se utiliza para seleccionar los anuncios que aparecerán en los sitios de un editor y determinar cuánto ganan con esos anuncios. Todos los anuncios pagan diferentes cantidades de dinero, dependiendo de factores como cuánto ha pujado un anunciante por el anuncio. El anuncio que gana es el que el usuario ve en el sitio web o la aplicación del editor.

Ad Manager utiliza el siguiente modelo de subasta para la subasta abierta y la subasta privada:

Ad Manager determina el pujador ganador en función de la puja neta más alta presentada. La puja neta refleja cualquier ajuste que, a su discreción, Ad Manager haya realizado en la puja presentada por el comprador con el fin de optimizar la subasta.

Independientemente de si se realizan ajustes, al comprador ganador nunca se le cobrará más que la oferta que presenta. Si los montos respectivos de las ofertas netas presentadas son los mismos, el ganador entre esas ofertas puede ser elegido al azar.

Para optimizar la subasta, Google puede optar por cerrar una subasta a un precio inferior al precio mínimo que de otro modo se habría aplicado. En tales casos, el comprador ganador puede pagar un precio inferior a la reserva y, por lo tanto, recibir un descuento en su oferta.

Un comprador que ha recibido descuento(s) en su(s) oferta(s) puede enfrentar precios de reserva más altos en transacciones posteriores para compensar dichos descuentos.

Sujeto a los términos que rigen su uso de la subasta de Google, a los vendedores se les paga el precio de cierre, neto de la participación en los ingresos de Google, pero no recibirán menos del precio de CPM que especificaron para la subasta. En el caso de que un vendedor desactive la configuración de participación en los ingresos promedio, las optimizaciones de subasta pueden dar lugar a que una subasta se cierre a un precio inferior al precio de reserva que de otro modo se habría aplicado.

Debido a que al Vendedor siempre se le pagará al menos su CPM mínimo especificado, el Vendedor puede recibir más de su participación en los ingresos contratados en la transacción.

En transacciones posteriores, la participación en los ingresos del Vendedor puede reducirse para compensar las ganancias anteriores que excedan la participación en los ingresos contratados, pero el Vendedor siempre recibirá al menos su participación en los ingresos contratados en todas sus transacciones de Compradores autorizados en un mes determinado.

Optimizar la subasta
Ad Manager puede ejecutar experimentos limitados diseñados para optimizar la subasta. Estos experimentos pueden incluir:

Modificación del modelo de subasta estándar o de la mecánica
Simulación de convocatorias de anuncios y subastas
modificar el precio de CPM establecido por el editor para una impresión o ajustar de otro modo la configuración del editor
descontar ciertas ofertas presentadas por los compradores o modificar de otro modo la prioridad de las ofertas presentadas por los compradores
La configuración de segmentación de anuncios del comprador no se modificará.

La subasta de anuncios se utiliza para seleccionar los anuncios que aparecerán en los sitios de un editor y determinar cuánto ganan con esos anuncios. Todos los anuncios pagan diferentes cantidades de dinero, dependiendo de factores como cuánto ha pujado un anunciante por el anuncio. El anuncio que gana es el que el usuario ve en el sitio web o la aplicación del editor.

Ad Manager determina el pujador ganador en función de la puja neta más alta presentada. La puja neta refleja cualquier ajuste que, a su discreción, Ad Manager haya realizado en la puja presentada por el comprador con el fin de optimizar la subasta.

Independientemente de si se realizan ajustes, al comprador ganador nunca se le cobrará más que la oferta que presenta. Si los montos respectivos de las ofertas netas presentadas son los mismos, el ganador entre esas ofertas puede ser elegido al azar.
Para optimizar la subasta, Google puede optar por cerrar una subasta a un precio inferior al precio mínimo que de otro modo se habría aplicado. En tales casos, el comprador ganador puede pagar un precio inferior a la reserva y, por lo tanto, recibir un descuento en su oferta.

Un comprador que ha recibido descuento(s) en su(s) oferta(s) puede enfrentar precios de reserva más altos en transacciones posteriores para compensar dichos descuentos.
Sujeto a los términos que rigen su uso de la subasta de Google, a los vendedores se les paga el precio de cierre, neto de la participación en los ingresos de Google, pero no recibirán menos del precio de CPM que especificaron para la subasta.

 # La tarea a realizar era:
 Realizar una muestra de data en Looker (ex Data Studio) del mercado de Ads en Ad Exchange.
 Para entender mejor primero hay que entender que es Ad Manager, es una plataforma de gestión de publicidad desarrollada por Google. Esta plataforma se utiliza para administrar y optimizar la entrega de anuncios publicitarios en línea en sitios web, aplicaciones móviles y otros medios digitales. Ad Manager se utiliza comúnmente en la industria de la publicidad en línea para ayudar a los editores de sitios web y aplicaciones a maximizar sus ingresos por publicidad al administrar y servir anuncios de manera eficiente. Los tipos de informes que se pueden obtener de allí son: 
* informe general abarca un panorama más amplio de todas las campañas publicitarias,
*  informe Ad Exchange se centra en los datos específicos de la plataforma de subastas de anuncios
*  informe Ad Server se enfoca en los datos de entrega y rendimiento de los anuncios entregados a los usuarios.


PASOS A SEGUIR:
   * Extracción de data de la API de la empresa, de Ad manager, con credenciales.Esto lo realice con python.Primero había que tener los NETWORK de cada empresa, una vez obtenida extraer los publisher o report service de cada uno de los clientes.
   *  Transformación de datos, también la realicé con python.
   *  Realicé dashboard en Looker Studio. Pautas del mismo:  El usuario puede filtrar dimensiones por: Fechas; Tipo de inventario (Video; In App, GPT; AMP; Null); Dispositivo;
       Primero se muestran valores netos sobre la data generla, luego comparación de cada empresa con respecto a la General, se puede seleccionar periodo a analisar, empresa, y país para ver el comportamiento en los distintos escenarios.
   También se muestra ganancias según tipo de inventario. Además analisé como se distribuyen las ganancias (RENUEVE) pudiendo filtrarse por empresa y país locual se muestra en un mapa para que sea mas ilustrativo, por último analisis de BIDS (ofertas) que realizó cada oferta, cuales fueron razones por las que fueron exitosas esas ofertas y en que paises se realiza mayor cantidad de ofertas. 
 
 

[La documentación para realizar el trabajo](https://developers.google.com/ad-manager/api/reporting?hl=es-419#creating_the_reportjob)


[Columnas y Dimensiones](https://developers.google.com/ad-manager/api/reference/v202305/ReportService.ReportQuery#columns)

Mi Informe:
````
  https://lookerstudio.google.com/reporting/6cf217fa-ac26-4dca-8c85-20cc8567b079


 
