
class RosMoWebInterface:
    def __init__(self):
        

    def webpage(self, dist):
        CSS = self.getCSS()
        CONTROL = self.controlTable()
        #Template HTML
        html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                <style>
                {CSS}
                </style>
                </head>
                <body>
                <div align = "center">
                <h1>RosMo</h1>
                {CONTROL}                
                
                </div>
                </body>
                </html>
                """
        return str(html)
    
    def BLANKpage(self, dist):
        CSS = self.getCSS()
        #Template HTML
        html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                <style>
                {CSS}
                </style>
                </head>
                <body>
                <div align = "center">
                <h1>RosMo</h1>
                PLEASE WAIT A TIC
                </div>
                </body>
                </html>
                """
        return str(html)
    
    
    def getCSS(self):
        css = "
         body {{
                color:#eae0c2;
                background-color: #1c1b18;
                font-family:Arial;
                font-size:14px;
                font-weight:bold;
            }}
  
            input {{
                box-shadow: 0px 1px 0px 0px #1c1b18;
                background:linear-gradient(to bottom, #eae0c2 5%, #ccc2a6 100%);
                background-color:#eae0c2;
                border-radius:15px;
                border:2px solid #333029;
                display:inline-block;
                cursor:pointer;
                color:#505739;
                font-family:Arial;
                font-size:14px;
                font-weight:bold;
                padding:12px 16px;
                text-decoration:none;
                text-shadow:0px 1px 0px #ffffff;
                width: 146px
            }}
            input:hover {{
                background:linear-gradient(to bottom, #ccc2a6 5%, #eae0c2 100%);
                background-color:#ccc2a6;
            }}
            input:active {{
                position:relative;
                top:1px;
            }}     
     
            .direction {{
                color:#FF00FF;
                font-size:20px;
                width: 50px;
            }}
            
            .control {{
                color:#FF00FF;
            }}
            "
        return str(css)
    
    def controlTable():
        control = "
          <h3 class='control'>Control</h3>
          <table><tr><td>            
           
            <table><tr><td>&nbsp;</td>
              <td><form action='./FW'><input type='submit' value='&uarr;' class='direction' /></form></td>
              <td>&nbsp;</td>
              </tr><tr>
              <td><form action='./L'><input type='submit' value='&larr;' class='direction' /></form></td>
              <td><form action='./STP'><input type='submit' value='&excl;' class='direction' /></form></td>
              <td><form action='./R'><input type='submit' value='&rarr;' class='direction' /></form></td>
              </tr><tr>
              <td>&nbsp;</td>
              <td><form action='./BK'><input type='submit' value='&darr;' class='direction' /></form></td>
              <td>&nbsp;</td>
              </tr>
            </table>
          </td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
          <td align = 'center'>
                &nbsp;&nbsp;&nbsp;&nbsp;Distance: {dist} cm &nbsp;&nbsp;&nbsp; <form action='./UPD'><input type='submit' value='Refresh' /></form>
           </td>
            </tr>
        </table>
        "
 