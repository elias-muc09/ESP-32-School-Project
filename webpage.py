
def web_page(ledred_state, ledfront_state, ledro1_state, ledro2_state):

    html_page = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="Control your ESP32 using a web interface.">
        <title>ESP32 Web Server</title>
        <meta name="favicon" href="https://omshingare.me/assets/logo-12777f7b.svg">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
        <style>
            body {{
                background-color: #121212;
                color: #ffffff;
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }}

            .container {{
                background-color: #1e1e1e;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
                padding: 20px;
                text-align: center;
            }}

            h2 {{
                color: #03a9f4;
            }}

            button {{
                font-size: 12px;
                padding: 6px 12px;
                margin: 3px;
            }}

            button.btn-success {{
                background-color: #4caf50;
            }}

            button.btn-danger {{
                background-color: #f44336;
            }}

            button.btn-warning {{
                background-color: #ff9800;
            }}

            p {{
                font-size: 14px;
                color: #ccc;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2 class="mt-4">ESP32 Web Server</h2>
            <p>This web interface allows you to control your ESP32 remotely.</p>
            
            <form class="mt-4">LED RED (<strong>{ledred_state}</strong>):
                <button class="btn btn-success" name="LEDRED" type="submit" value="1">LED ON</button>
                <button class="btn btn-danger" name="LEDRED" type="submit" value="0">LED OFF</button>
            </form>
            
            <form class="mt-4">LED Front (<strong>{ledfront_state}</strong>):
                <button class="btn btn-success" name="LEDFRONT" type="submit" value="1">LED ON</button>
                <button class="btn btn-danger" name="LEDFRONT" type="submit" value="0">LED OFF</button>
            </form>            
            
            <form class="mt-4">LED Room 1 (<strong>{ledro1_state}</strong>):
                <button class="btn btn-success" name="LEDRO1" type="submit" value="1">LED ON</button>
                <button class="btn btn-danger" name="LEDRO1" type="submit" value="0">LED OFF</button>
                <button class="btn btn-warning" name="LEDRO1" type="submit" value="GREEN">LED GREEN</button>
                <button class="btn btn-warning" name="LEDRO1" type="submit" value="RED">LED RED</button>
                <button class="btn btn-warning" name="LEDRO1" type="submit" value="BLUE">LED BLUE</button>
                <button class="btn btn-warning" name="LEDRO1" type="submit" value="SHOW">SHOW</button>
            </form>

            <form class="mt-4">LED Room 2 (<strong>{ledro2_state}</strong>):
                <button class="btn btn-success" name="LEDRO2" type="submit" value="1">LED ON</button>
                <button class="btn btn-danger" name="LEDRO2" type="submit" value="0">LED OFF</button>
                <button class="btn btn-warning" name="LEDRO2" type="submit" value="GREEN">LED GREEN</button>
                <button class="btn btn-warning" name="LEDRO2" type="submit" value="RED">LED RED</button>
                <button class="btn btn-warning" name="LEDRO2" type="submit" value="BLUE">LED BLUE</button>
                <button class="btn btn-warning" name="LEDRO2" type="submit" value="SHOW">SHOW</button>
            </form>

        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>"""

    return html_page


