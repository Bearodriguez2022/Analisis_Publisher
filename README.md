# Analisis_Publisher
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
   *  Transformación de datos, también larealicé con python.
   *  Realicé dashboard en Looker Studio. Pautas del mismo:  El usuario puede filtrar dimensiones por: Fechas; Tipo de inventario (Video; In App, GPT; AMP; Null); Dispositivo;
 Geo y si quiere puede seleccionar: “comparar contra mi inventario”.
 Primero se muestran valores netos (teniendo en cuenta los filtros aplicados a las dimensiones) sobre la data generla:
 U$D eCPM; %Fill Rate; U$D Request RPM; Bid vs Request rate Vs (debajo); U$D Average Bid eCPM valores netos
 en colores (verde si es superior, negro si es neutro, Rojo si es inferior) de las mismas métricas pero solo con el
 inventario del publishers y al costado de cada uno la diferencia % entre si.
 Debajo un gráfico de barras por día con una métrica que el usuario puede seleccionar entre:U$D eCPM; % Fill Rate;
 U$D Request RPM; #Bid/Request rate; U$D Average bid CPM VS la misma métrica por día del inventario del
 publisher.
 Debajo un gráfico de filled area donde el color del país esta en degradé de tono más oscuro a más claro para
 mostrar la relación entre los países bajo la misma métrica que el usuario seleccionó entre: U$D eCPM; % Fill Rate;
 U$D Request RPM; #Bid/Request rate; U$D Average bid CPM y la misma métrica con respecto al inventario del
 publisher.. En texto dentro de cada país se coloca el valores general y del inventario del publisher para esa métrica
 en ese país.
 Debajo un gráficos de donut chat que tiene las Bid Rejection Reason distribuidas proporcionalmente.
 debajo grafico de staked colum chat por bid range (son de a 0,10 USD, comenznado en 0 y termina en el valor
 máximo que hayan ofrecido por el inventario). Dentro de cada rango hay una columna apilada con el valor de
 Average Bid CPM USD del inventario general vs el inventario del publisher.
