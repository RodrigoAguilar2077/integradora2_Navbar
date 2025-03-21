from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mail import Mail, Message


app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Servidor SMTP de Gmail
app.config['MAIL_PORT'] = 587  # Puerto SMTP para TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'futech2026@gmail.com'  # Cambia esto con tu correo
app.config['MAIL_PASSWORD'] = 'svwk qvmy obbe mtgp'  # Contraseña o App Password de tu correo
app.config['MAIL_DEFAULT_SENDER'] = 'futech2026@gmail.com'

mail = Mail(app)

# Ruta para procesar el formulario
@app.route('/enviar_correo', methods=['POST'])
def enviar_correo():
    if request.method == 'POST':
        nombre = request.form['name']
        correo = request.form['email']
        mensaje = request.form['message']
        
        # Crear el mensaje
        msg = Message('Nuevo mensaje de AUTOPET UTT', recipients=['futech2026@gmail.com'])
        msg.body = f"""
        Nombre: {nombre}
        Correo: {correo}
        Mensaje: {mensaje}
        """

        try:
            mail.send(msg)
            flash('¡Tu mensaje ha sido enviado exitosamente! 🎉', 'success')
            return redirect(url_for('index'))  # Cambia a la ruta correcta si es necesario
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            flash('Hubo un error al enviar tu mensaje. 😢', 'danger')
            return redirect(url_for('home'))
        
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
