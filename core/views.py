from django.shortcuts import render

# TAREA PENDIENTE: Conectar datos a la base de datos SQLite

NOMBRE_DEL_SITIO = 'Librotek'

def titulo(subtitulo=None):
    if subtitulo is None:
        return NOMBRE_DEL_SITIO
    return f'{NOMBRE_DEL_SITIO} - {subtitulo}'

# Views

def index(request):
    return render(request, 'core/index.html',
        {
            'titulo': titulo(),
            'subtitulo': 'Bienvenidos a Librotek'
        }
    )

def historia(request):
    tarjetas = [
        {
            'imagen': '/static/core/img/meditaciones.jpg',
            'titulo': 'Meditaciones',
            'descripcion': 'El emperador y filósofo romano Marco Aurelio destacó por su serenidad, su modestia y su búsqueda de la verdad, a la vez que fue un césar brillante en el campo de batalla. Solo escribió una obra: Meditaciones, uno de los mejores libros de filosofía y ética de la historia. Se trata de un compendio de sabiduría y reflexión para afrontar los tiempos adversos. Sus principios estoicos siguen estando vigentes en la actualidad: cómo mantener la integridad, cómo ser tolerante, cómo conservar la calma, cómo vivir en armonía el presente, actuando sobre lo que depende de uno y aceptando lo que no. En definitiva, una obra maestra para comprender mejor nuestra alma.',
            'precio': 'Invaluable',
        },
        {
            'imagen': '/static/core/img/hissig.jpg',
            'titulo': 'Historia del Siglo XX',
            'descripcion': 'Una obra excepcional para comprender el siglo XX, de la mano del gran historiador de nuestra época Eric Hobsbawm.Eric Hobsbawm, el gran historiador británico, es, quizás, uno de los pocos profesionales que podía enfrentarse al estudio de una época histórica de la que todavía, autor y lectores, formamos parte. Lo ha hecho con un gran conocimiento de la bibliografía, especializada y no especializada, y con sus propias experiencias y observaciones, que ha sabido entrelazar hábilmente en una síntesis magistral en la que se avanza con creciente expectación. Su obra abunda en análisis incisivos, basados en sólidos argumentos y desprovistos de la inhibición ante hechos que tradicionalmente se han considerado como demasiado cercanos para opinar sobre ellos. Hobsbawm opina y juzga y lo hace, como quiere Vilar, sólo después de haber comprendido. Desde aquellos diez días que conmovieron al mundo hasta el umbral mismo del tercer milenio, el profesor Hobsbawm recorre todo lo que él llama «el siglo XX corto» en una obra que, aún antes de aparecer en inglés, ya había merecido los elogios más entusiastas de la crítica, y cuya edición española se publicó en el 50 aniversario del fin de la segunda guerra mundial.',
            'precio': '$25.000',
        },
    ]
    return render(request, 'core/categoria.html',
        {
            'titulo': titulo('Historia'),
            'subtitulo': 'Historia',
            'tarjetas': tarjetas
        }
    )

def fantasia(request):
    tarjetas = [
        {
            'imagen': '/static/core/img/cuentosfan.jpg',
            'titulo': 'Cuentos de Fantasía',
            'descripcion': 'La fascinación del hombre por lo desconocido, lo sobrenatural y lo extraordinario viene casi desde el principio de los días. El ser humano siempre ha buscado el porqué de su existencia, la razón última de por qué y para qué está en este mundo. Ahí nació nuestra curiosidad por todo lo que no se ve, pero que gravita entorno a nuestra existencia. El alma humana o los dioses, por ejemplo. Eso estimuló nuestra imaginación y pronto empezamos a crear toda una suerte de seres ficticios que empezaron a poblar las leyendas que se trasmitían de forma oral, de unos a otros. A saber: duendes, hadas, demonios, y un largo etcétera de mitos que desde entonces forman parte de nuestra cultura popular y dieron lugar al género fantástico.',
            'precio': '$20.000',
        },
        {
            'imagen': '/static/core/img/fantasma.jpg',
            'titulo': 'El Fantasma del Coliseo',
            'descripcion': '¡El fantasma de un gladiador amenaza el Coliseo! ¡Por mil quesos de bola, por el Coliseo vaga el terrible Gladiador Fantasma y ningún turista quiere visitarlo ya! Hay que hacer algo... Esta es una misión especial para mí, ¡el agente secreto Cero Cero G!',
            'precio': '$25.000',
        },
    ]
    return render(request, 'core/categoria.html',
        {
            'titulo': titulo('Fantasia'),
            'subtitulo': 'Fantasia',
            'tarjetas': tarjetas
        }
    )

def manuales(request):
    tarjetas = [
        {
            'imagen': '/static/core/img/manual.jpg',
            'titulo': 'Manual de Carreño',
            'descripcion': 'Escrito hace más de 150 años y conocido originalmente como Manual de urbanidad y buenas maneras, este clásico sigue vigente hoy en día, no solo como documento histórico, sino también por el espíritu de fondo que lo guía: promover una mejor convivencia social basada en el respeto mutuo. Tal es el espíritu que ha motivado presentar esta edición renovada que, por un lado, revisa cada una de las entradas del autor, rescatando una obra que ha acompañado, generación tras generación, a quienes les preocupa demostrar su buena educación; y, por otro lado, incluye nuevas entradas modernizadas, ofreciendo una guía actual de códigos de conducta en las ciudades de hoy, como la “netiqueta” o comportamiento en las redes sociales, las reglas para convivir en los medios de transporte, la oficina, los gimnasios, el uso del celular, la tenencia responsable de mascotas y otras.',
            'precio': '$20.000',
        },
        {
            'imagen': '/static/core/img/enqui.jpg',
            'titulo': 'Manual o Enquiridion',
            'descripcion': 'La moral estoica nació en grecia hacia el siglo iii a. c. y tuvo amplia influencia en las élites romanas del siglo ii d. c. para ella, el dominio de las pasiones y el alejamiento de lo superfluo permitiría cumplir con el orden universal (logos) impuesto a la naturaleza (physis). de este modo, ética, física y lógica conformaban un todo indisoluble para el ser humano donde vivir según la razón o la virtud será vivir según la naturaleza. en la historia de la humanidad muchos pensadores se han guiado por estos principios desde agustín de hipona hasta nuestros contemporáneos andré malraux y albert camus, pasando por descartes, kant y spinoza por nombrar a algunos. esta versión del enquiridion es fruto del trabajo de traducción de hernán soto. epicteto fue un filósofo griego que vivió entre el año 50 y 140 de nuestra era. llevado a roma como esclavo, fue liberado por su amo impresionado de su inteligencia y capacidad. posteriormente será expulsado junto a otros filósofos por promover desórdenes. de regreso en grecia dio clases y ejemplos de vida conforme a sus ideales hasta su muerte.',
            'precio': '$25.000',
        },
    ]
    return render(request, 'core/categoria.html',
        {
            'titulo': titulo('Manuales'),
            'subtitulo': 'Manuales',
            'tarjetas': tarjetas
        }
    )

def novelas(request):
    tarjetas = [
        {
            'imagen': '/static/core/img/aje.jpg',
            'titulo': 'Novela de Ajedrez',
            'descripcion': 'Un crucero que cubre la ruta de Nueva York a Buenos Aires es el escenario de una singular partida de ajedrez. El arrogante campeón del mundo, que acude a la capital argentina a defender su título, se enfrenta a un pomposo millonario escocés y al narrador de la historia.\nAl unirse un misterioso pasajero cuyo juego maravilla a todos los contendientes, sobreviene uno de los giros argumentales más estremecedores de la historia de la literatura.\nNovela de ajedrez es la obra póstuma de Stefan Zweig, un tremendo pero fascinante alegato contra el horror nazi que retrata con suma delicadeza los sentimientos y la naturaleza humana.',
            'precio': '$20.000',
        },
        {
            'imagen': '/static/core/img/afri.jpg',
            'titulo': 'Africanus',
            'descripcion': 'La obra maestra de la novela histórica A finales del siglo III a. C., Roma se encontraba al borde de la destrucción total, a punto de ser aniquilada por los ejércitos cartagineses al mando de uno de los mejores estrategas militares de todos los tiempos: Aníbal. Su alianza con Filipo V de Macedonia, que pretendía la aniquilación de Roma como Estado y el reparto del mundo conocido entre las potencias de Cartago y Macedonia, constituía una fuerza imparable que, de haber conseguido sus objetivos, habría determinado para siempre el devenir de Occidente. Pero el azar y la fortuna intervinieron para que las cosas fueran de otro modo. Pocos años antes del estallido del más cruento conflicto bélico que se hubiera vivido en Roma, nació un niño que estaba destinado a cambiar el curso de la Historia: Publio Cornelio Escipión, a quien se conocerá como Africanus.',
            'precio': '$25.000',
        },
    ]
    return render(request, 'core/categoria.html',
        {
            'titulo': titulo('Novelas'),
            'subtitulo': 'Novelas',
            'tarjetas': tarjetas
        }
    )

def psicologia(request):
    tarjetas = [
        {
            'imagen': '/static/core/img/psi.jpg',
            'titulo': 'Psicologia de la Posible Evolucion del Hombre',
            'descripcion': 'Para quien se acerca por primera vez a la enseñanza de Gurdjieff, este libro es ideal. Con notable claridad y síntesis, ofrece una panorámica de sus ideas fundamentales y propone ejercicios prácticos para constatarlas. En cinco conferencias enfoca su atención sobre los diferentes estados de conciencia, la mendicidad, el recuerdo de sí, el estudio de los diferentes centros del hombre y su división en siete categorías, siempre desde el punto de vista de lo que él puede llegar a ser. Una vez que se da cuenta de que no tiene prácticamente ningún control sobre las circunstancias exteriores ni los estímulos internos, el ser humano puede encontrar y transitar un camino que le permita trabajar con un grupo para liberarse de esta vida mecánica y alcanzar la unidad interior. no hay evolución obligatoria, mecánica. La evolución es el resultado de una lucha consciente. La naturaleza no necesita esta evolución. No la quiere y la combate. G.I. Gurdjieff.',
            'precio': '$25.000',
        },
        {
            'imagen': '/static/core/img/lac.jpg',
            'titulo': 'Lacan: El amo Absoluto',
            'descripcion': 'Más que como una introducción, este libro puede leerse como una "forma de acceso al pensamiento de Lacan".La dimensión que tiene Hegel, leído por Kojeve, y por sobre el hombro de Heidegger, en el pensamiento de Lacan, es así una cara que es trabajada brillantemente por Borch-Jacobsen, quien trae a la luz fuentes y conceptos que se traducen no sólo en toda la dialéctica del Amo y del Esclavo, sino, sobre todo, en la concepción del deseo, lo real y la verdad en Lacan, fundamentales para su idea del sujeto.La seriedad y la formación del autor, y su fidelidad a los textos de Freud y de Lacan, traen el resguardo de una operación de honesto trabajo intelectual que nos revela facetas escondidas de un pensamiento.Frente a versiones repetitivas y canonizantes de los “partidarios” de un gran pensador,  resultan más fructíferos los análisis de críticos que lo estudien desde fuera del movimiento por él creado, como ya lo había observado el mismo Lacan acerca de su “Instancia de la letra”.',
            'precio': '$25.000',
        },
    ]
    return render(request, 'core/categoria.html',
        {
            'titulo': titulo('Psicologia'),
            'subtitulo': 'Psicologia',
            'tarjetas': tarjetas
        }
    )

def registro(request):
    return render(request, 'core/registro.html',
        {
            'titulo': titulo('Registro'),
            'subtitulo': 'Registro'
        }
    )

def sesion(request):
    return render(request, 'core/sesion.html',
        {
            'titulo': titulo('Sesion'),
            'subtitulo': 'Sesion'
        }
    )
