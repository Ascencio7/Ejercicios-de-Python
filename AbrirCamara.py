# Ejecutar el comando en la terminal para que funcione: pip install opencv-python

# Importar la biblioteca OpenCV
import cv2

# Se inicializa la cámara. El argumento '0' indica que se usará la cámara predeterminada de la laptop
cap = cv2.VideoCapture(0)

# Se verifica si la cámara se abrió correctamente
if not cap.isOpened():
    print("No se puedo abrir la cámara.")  # Un mensaje de error si no se puede acceder a la cámara
    exit()  # Salir del programa si no se puede abrir la cámara

# Un bucle infinito para capturar y mostrar frames continuamente
while True:
    # Capturar un frame de la cámara
    ret, frame = cap.read()
    # 'ret' es un booleano que indica si el frame se capturó correctamente
    # 'frame' es la imagen capturada

    # Si no se pudo capturar el frame, salir del bucle
    if not ret:
        print("No se pudo recibir el frame. Saliendo...")
        break

    # Se muestra el frame capturado en una ventana llamada 'Cámara'
    cv2.imshow('Cámara', frame)

    # Se espera 1 milisegundo y verificar si se presionó la tecla 'q'
    # Si se presiona 'q', se sale del bucle
    if cv2.waitKey(1) == ord('q'):
        break

# Se libera la cámara para que pueda ser usada por otras aplicaciones
cap.release()

# Se cierra todas las ventanas abiertas por OpenCV
cv2.destroyAllWindows()