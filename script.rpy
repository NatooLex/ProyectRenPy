

define M = Character("Maya",color="#d133ff",who_font="vineritc.ttf")
define narrator = Character(what_italic=True)
define slowdissolve = Dissolve(0.5)
define R = Character("[name]",who_font="vineritc.ttf",what_outlines=[(1,"#A5B2AE",0,0)])
define A = Character ("?")
define R_shout = Character("[name]",what_size=25,who_font="vineritc.ttf")
define R_whisper = Character("[name]", what_size=18)
define R_red = Character("[name]",what_color="#FA1D1A") 
define Al = Character("Alvaro",who_font="vineritc.ttf")
label start:

    
    
    scene mya room
    with slowdissolve

    

    show maya happy:
        xalign 0.5
        yalign 0.5
    with slowdissolve
  
    play music "menuLoop.mp3" fadeout 1

    
    
    # Presenta las líneas del diálogo.
    
    
    
    python:
        name = renpy.input(_("Cual es tu nombre? (Nombre Generico - David)"))

        name = name.strip() or "David"
 
    M "Hola [name]."

    menu:
        M "Bienvenido a {b}Vida Utópica{/b}, ¿desde dónde descargaste el juego?"
            
        "Me lo enviaron.":
                         jump choice1_yes

        "Desde Mediafire xD.":
                             jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        M "¿En serio? Supongo que habrá sido el creador."

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        M "Maravillosa jugada, {w=1.0}pero no está subido a Mediafire, ¿o sí? "

        jump choice1_done

    label choice1_done:

    menu:
        M "¿Eres joven?"
        
        "Si":
            jump choice2_yes
        
        "No":
            jump choice2_no
    
    label choice2_yes:
        
        $ menu_flag = True
        
        M "Quizas sea mejor, ya que podrías entender mejor la historia."
        
        jump choice2_done

    label choice2_no:
    
        $ menu_flag = False
        
        M "Vaya, ojalá trates de entender la historia, lo tratamos de hacer para todas las edades."
        
        jump choice2_done
      
    label choice2_done: 
        
        
    M "Esto es solo una introducción, a un juego que tiene preparado NatooLex, el creador."
        
    R "¿En serio?, ¿podrías contarme un poco?"
        
    
    M "Claro!" 
    
    M "Se tratará de un estudiante, que no era tan reconocido en su escuela, y que en un día, su vida cambió por completo."
        
    R "Mmm... se parece a alguien que conozco..."

    M "Oh, no pienses en eso, igualmente, si el juego tiene algo de similitud con la vida real, es pura coincidencia."
        
    M "{w=1.0} Eso creo..."
        
    M "Ah y claro, el juego no tiene el objetivo de ofender a nadie."
        
    M " Y recalcar que es una novela visual, que se estará actualizando. Como solo es uno el que modifica scripts, hacer minijuegos en la historia será complicado."
        
    M "Y sí... un saludo especial a Pacheco por el apoyo de este proyecto, cerebro creativo de la historia."
        
    "Oye, tenemos que irnos."
    
    M "Me estaba gustando la conversación, bueno, nos vemos [name], diviertete y ojalá te guste."
    
    M "Y se me olvidaba, sigue a NatooLex en {a=https://twitter.com/NatooLex}Twitter{/a} para mas info. Chau."
    
    
    stop music
    scene pla lluvia
    with slowdissolve
    
    
    "Noche lluviosa."
    
    "Pero... eso ni a ti te interesaba, tu hacías un test online en dúo para un concurso."
    
    "Era muy estricto, sin ningún tipo de aparato electrónico, o eras descalificado automaticamente."
    
    "Te preguntarás que, como van a saber si lo estas ocupando o no?, bueno... {w=1.0} como sea, vamos con la historia."
    
    play music "song1.mp3" fadeout 1
    scene pla room1
    with slidedown
    
    R "Mmm... 42 + 90? Tengo 5 segundos."
    
    A  "122."
    
    menu:
        R "Creo que no..."
        
        "Es 132.":
                 jump choice3_yes
        
        "Es 142.":
                 jump choice3_no
        
        "Es 152.":
                 jump choice3_no
        
        "Espera, claro que es 122.":
                 jump choice3_vno
        
    label choice3_yes:
    
        $ menu_flag = True 
        
        A  "Estas seguro?"
        
        "Tú le das a esa opción."
        
        R "Bien! 49 de 50 ejercicios buenos."
        
        A "Y yo que no confiaba en tí."
        
        R "Igualmente nos equivocamos en una, voy a ver como va la clasificación."
        
        scene pla roomwin
        
        R_shout "¡Vamos primeros! Si quedamos entre los cinco mejores, ganaríamos el concurso."
        
        jump story_central1
        
    label choice3_no:
       
        $ menu_flag = False
        
        A "Seguro."
        
        "Tu , sin dudarlo, le das a esa opción."
        
        R "No! Otra vez en las fáciles."
        
        A "Y más encima era 132."
        
        R "48 de 50 ejercicios buenos..."
        
        jump choice3_done
        
    label choice3_vno:
    
        $ menu_flag = False
        
        A "¿Lo ves? Dale nomás."
        
        "Igualmente, con dudas, le das a esa opción."
        
        R "No era! Y confié en tí."
        
        A "Pero no me eches la culpa, pensabas que estabas seguro."
        
        R "48 de 50 ejercicios buenos..."
        
        jump choice3_done
        
    label choice3_done:
        
    R "Igualmente nos equivocamos en dos, voy a ver como va la clasificación."
    
    scene pla roomlose
        
    R "Bueno, estamos terceros, igualmente podríamos ganar el concurso, pero será complicado."
    
    jump story_central1
    
    label story_central1:
    scene pla roomend

    A "Nos vemos mañana, me tengo que ir a dormir... es bien tarde."
    
    R "Vale Alvaro, nos vemos mañana en el liceo."
        
    "Para contextualizarte más, no sueles relacionarte con mucha gente, pero tampoco te interesa demasiado. Tú mejor amigo es Alvaro, tu compañero de curso."
    
    "Sueles pasar todo el día hablando sobre distintos temas con él. Los dos suelen ser muy parecidos en sus gustos."
    
    "Ah, y no te había dicho... tienes 17 años. Según tú, eres bueno en los videojuegos y eres buena gente. Te tratas de esforzar lo maximo en todo."
    
    "Mañana es Lunes, una nueva semana... {w=1.0} pero no sabrías lo que cambiaría tu vida en estos días."
    
    scene bla black
    
    "LUNES 7:00 AM."
    
    scene pla room2
    
    R "Que lata otra vez, ojalá haya un despachito y su Fortnite devuelta a casa."
    
    "Tu colegio no suele ser normal. Hay un grupo que está causando un caos, y que no deja continuar con las clases normales."
    
    "Su justificación suele ser, que están ayudando a la educación pública, y luchando por sus derechos."
    
    "Pero cada uno tiene su opinión."
    
    scene pla metro
    
    R "El metro va súper lleno, no es novedad."
    
    "Hubo ALGUIEN que te llamó la atención, pero decidiste un momento después no prestar importancia."
    
    scene pla in
    
    "Llegas a tu liceo... {w=1.0}... {w=1.0} ¿en serio creías que no habría algo con la realidad? Que ingenuo."
    
    R "Justo a la hora. Ojalá haya una asamblea a las 7:45."
    
    scene pla classroom
    
    "Cuando entras a la sala, Alvaro te empieza a hablar rápidamente."
    
    Al "Acaban de hacer un torneo de Fortnite en el IN. Deberías participar. Son 100.000 pesos en premios. Patrocina Entel y ACE."
    
    "Jajajaja, ya no sé si esto es ficticio o no."
    
    R "¿Estas webeando?"
       
    Al "Y dicen que si ganas el torneo, creo que directamente entras en el equipo de ACE de Fortnite."
    
    "ACE es catalogado como unos de los mejores equipos de eSports de Chile."
    
    R "¿Te imaginas? Ganando el torneo, llegando a un equipo profesional. Es demasiado bonito para ser real, pasaría solo en juegos."
    
    "¿O no?"
    
    R "Mañana es el aniversario del colegio. Supondría que mañana es el torneo."
    
    Al "Exacto, aunque te advierto que habrá demasiado nivel. Vendrá incluso gente externa al IN a competir."
    
    R "Ya ves, y eso que estoy jugando poco. La música te quita mucho tiempo."
    
    Al "¿En serio? Tocando piano supongo."
    
    R "Es el único instrumento que se me da bien."
    
    "Seguían charlando sobre distintos temas. Después de cada clase ibas a tomar un poco de aire. Hasta que llegó el final de la jornada."
    
    R "Que raro que no hubo capuchas en todo el día."
    
    Al "Solo espera una hora más, y ya verás que aparecen."
    
    R "Quizás cuando llegue a la casa, recien vayan apareciendo. Nos vemos mañana."
    
    Al "Acuerdate del concurso, dan los resultados definitivos esta noche. Chao."
    
    "Hacías tu rutina diaria, metro, tomabas una micro y llegabas a tu casa."
    
    show pla tv
    
    R "Prenderé la tele a ver que está pasando."
    
    show pla tvon
    
    R "Vaya, ya esto es cotidiano."
    
    "Basado en hechos reales, kie pero kie."
    
    show pla tvon2
    
    R "Los medios nos están tratando como delicuentes."
    
    "Se vendrá una decisión importante, por favor, piensalo bien."
    
    menu:
        R "Pero pienso que los capuchas..."
        
        "Deberiamos apoyarlos.":
                               jump capucha_story
                               
                               
        "Deberían ser capturados.":
                                  jump main_story
        
    label capucha_story:
    
    R "Deberíamos apoyarlos, están haciendo un bien para nuestra educación."
    
    R "Quizás no sea una decisión muy inteligente, ya que la opinión pública está por el piso, pero creo que podemos seguir luchando por la causa. No hay otra forma que la violencia."
    
    stop music
    scene pla piano
    play music "piano1.mp3" fadeout 1
    
    "Almorzaste, te bañaste, estudiaste y empezaste a tocar piano."
    
   
    "..."
    
    "..."
    
    "..."
    
    "..."
    
    stop music
    scene pla fortnite
    
    R "Debería empezar a practicar para el torneo de mañana."
    
    play music "song1.mp3" fadeout 1
    
    "Prendiste la PS4 y jugaste 2 horas."
    
    scene pla sleep
    
    R "Ya es tarde, debería dormirme."
    
    "MARTES 7:00 AM"
    
    
    
    
    
    
    return
