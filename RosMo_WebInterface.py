#********************************************************
#        web page builder for RosMo Control
#               Alex Just-Alex Dec 2024
#********************************************************

interface = "PC" 
speed = 0.5

def webpage(dist):
    global interface
    print("INTFC: " + interface)
    if interface == "phone":
        return phonepage(dist)
    CSS = getCSS()
    CONTROL = controlTable(dist)
    # Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>RosMo Control</title>
            <style>
            {CSS}
            </style>
            </head>
            <body>
            <div align="center">
            <h1>RosMo (PC interface)</h1>
            {CONTROL}  
            </div>
            </body>
            </html>
            """
    return str(html)

def phonepage(dist):
    CSS = getCSS()
    CONTROL = controlTable(dist)
    # Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>RosMo Control</title>
            <style>
            {CSS}
            </style>
            </head>
            <body>
            <div align="center">
            <h1>RosMo (Phone interface)</h1>
            {CONTROL}
            </div>
            </body>
            </html>
            """
    return str(html)

def BLANKpage():
    CSS = getCSS()
    # Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <style>
            {CSS}
            </style>
            </head>
            <body>
            <div align="center">
            <h1>RosMo</h1>
            PLEASE WAIT FOR CURRENT COMMAND TO COMPLETE
            </div>
            </body>
            </html>
            """
    return str(html)

def getCSS():
    css = """
     body {
            color:#eae0c2;
            background-color: #1c1b18;
            font-family:Arial;
            font-size:28px;
            font-weight:bold;
            margin: 0;
            padding: 0;
        }

        input {
            box-shadow: 0px 1px 0px 0px #1c1b18;
            background:linear-gradient(to bottom, #eae0c2 5%, #ccc2a6 100%);
            background-color:#eae0c2;
            border-radius:15px;
            border:2px solid #333029;
            display:inline-block;
            cursor:pointer;
            color:#505739;
            font-family:Arial;
            font-size:16px;
            font-weight:bold;
            padding:40px 20px; /* Doubled padding for twice the depth */
            text-decoration:none;
            text-shadow:0px 1px 0px #ffffff;
            width: 100%;
            box-sizing: border-box;
            margin: 10px 0; /* Added margin for spacing */
        }
        input:hover {
            background:linear-gradient(to bottom, #ccc2a6 5%, #eae0c2 100%);
            background-color:#ccc2a6;
        }
        input:active {
            position:relative;
            top:1px;
        }     
 
        .direction {
            color:#444444; /* Changed to dark grey */
            font-size:20px;
        }  
 
        .speed {
            color:#444444; /* Changed to dark grey */
            font-size:20px;
        }
        .control {
            color:#444444; /* Changed to dark grey */
        }
        table {
            width: 100%;
        }
        td {
            padding: 5px;
        }
        """
    return str(css)

def controlTable(dist):
    global interface
    global speed
    if speed < 0.5:
        speedstr = "slow"
    elif speed > 0.5:
        speedstr = "fast"
    else:
        speedstr = "medium"

    if interface == "phone":
        link = "<form action='./PC'><input type='submit' value='PC Interface' /></form>"
    else:
        link = "<form action='./PH'><input type='submit' value='Phone Interface' /></form>"

    control = f"""
      <h3 class='control'>Control</h3>
      <table>
        <tr>
          <td>
            <form action='./CL'><input type='submit' value='&nwarhk;' class='direction' /></form>
          </td>
          <td>
            <form action='./FW'><input type='submit' value='&uarr;' class='direction' /></form>
          </td>
          <td>
            <form action='./CR'><input type='submit' value='&nearhk;' class='direction' /></form>
          </td>
        </tr>
        <tr>
          <td>
            <form action='./L'><input type='submit' value='&olarr;' class='direction' /></form>
          </td>
          <td>
            <form action='./STP'><input type='submit' value='&excl;' class='direction' /></form>
          </td>
          <td>
            <form action='./R'><input type='submit' value='&orarr;' class='direction' /></form>
          </td>
        </tr>
        <tr>
          <td colspan="3">
            <form action='./BK'><input type='submit' value='&darr;' class='direction' /></form>
          </td>
        </tr>
        <tr>
          <td>
            <form action='./SS'><input type='submit' value='slow' class='speed' /></form>
          </td>
          <td>
            <form action='./SM'><input type='submit' value='medium' class='speed' /></form>
          </td>
          <td>
            <form action='./SF'><input type='submit' value='fast' class='speed' /></form>
          </td>
        </tr>
      </table>
      <div align="center" style="margin-top: 20px;">
        Distance: {dist} cm (not implemented)<br />
        Speed: {speedstr}<br /><br />
        <form action='./UPD'><input type='submit' value='Refresh' /></form>
        <br /><br />
        {link}
      </div>
    """
    return str(control)

