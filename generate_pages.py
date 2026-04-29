import re

with open("auf-tirol-site_index.html", "r") as f:
    content = f.read()

head_match = re.search(r'(<!DOCTYPE html>.*?<style>.*?</style>)', content, re.DOTALL)
if head_match:
    head_content = head_match.group(1)
else:
    head_content = "<!DOCTYPE html>\n<html>\n<head><title>Page</title></head>"

extra_styles = """
    .legal-content { padding: 60px 0; max-width: 800px; margin: 0 auto; font-family: Inter, Arial, Helvetica, sans-serif; color: var(--text); }
    .legal-content h1 { font-size: 36px; margin-bottom: 30px; }
    .legal-content h2 { font-size: 24px; margin-top: 40px; margin-bottom: 16px; border-bottom: 1px solid var(--border); padding-bottom: 8px; }
    .legal-content h3 { font-size: 20px; margin-top: 30px; margin-bottom: 12px; }
    .legal-content p, .legal-content li { color: var(--muted); margin-bottom: 16px; font-size: 16px; line-height: 1.6; }
    .legal-content a { color: var(--accent); }
    .legal-content table { width: 100%; border-collapse: collapse; margin-bottom: 24px; }
    .legal-content th, .legal-content td { text-align: left; padding: 12px; border: 1px solid var(--border); color: var(--muted); }
    .legal-content th { background: var(--panel); color: var(--text); }
    .back-btn { display: inline-block; margin-bottom: 40px; color: var(--muted); text-decoration: none; font-weight: 600; padding: 10px 20px; border: 1px solid var(--border); border-radius: 12px; background: var(--panel); transition: 0.2s ease; }
    .back-btn:hover { background: var(--panel-strong); color: var(--text); }
</head>
<body style="background: var(--bg);">
  <div class="container legal-content">
    <a href="auf-tirol-site_index.html" class="back-btn">&larr; Zurück zur Startseite</a>
"""

impressum_body = """
    <h1>Impressum</h1>
    
    <p><strong>[Firmenname, Name der Person]</strong><br>
    [Adresse, PLZ, Ort]</p>

    <p><strong>Unternehmensgegenstand:</strong> []<br>
    <strong>UID:</strong> [Umsatzsteuer ID einfügen (wenn vorhanden)]<br>
    <strong>Tel.:</strong> [Telefonnummer einfügen]<br>
    <strong>E-Mail:</strong> [Email einfügen]</p>

    <p><strong>Mitglied bei:</strong> [Kammerorganisation einfügen (wenn vorhanden)]<br>
    <strong>Berufsrecht:</strong> Gewerbeordnung: <a href="https://www.ris.bka.gv.at" target="_blank">www.ris.bka.gv.at</a><br>
    <strong>Aufsichtsbehörde/Gewerbebehörde:</strong> [Bezirkshauptmannschaft einfügen]</p>
    
    <h2>Konzeption & Umsetzung</h2>
    <p>JAY Solution GmbH - Wir digitalisieren KMU!<br>
    Eduard-Bodem-Gasse 1<br>
    6020 Innsbruck<br>
    Österreich</p>
    <p><strong>Tel:</strong> +43 512 312001<br>
    <strong>Mail:</strong> office@jay-solution.com<br>
    <strong>Web:</strong> <a href="http://www.jay-solution.com" target="_blank">www.jay-solution.com</a></p>

    <h2>EU-Streitschlichtung</h2>
    <p>Gemäß Verordnung über Online-Streitbeilegung in Verbraucherangelegenheiten (ODR-Verordnung) möchten wir Sie über die Online-Streitbeilegungsplattform (OS-Plattform) informieren.<br>
    Verbraucher haben die Möglichkeit, Beschwerden an die Online Streitbeilegungsplattform der Europäischen Kommission unter <a href="https://ec.europa.eu/consumers/odr" target="_blank">https://ec.europa.eu/consumers/odr</a> zu richten.<br>
    Die dafür notwendigen Kontaktdaten finden Sie in unserem Impressum. Wir möchten Sie jedoch darauf hinweisen, dass wir nicht bereit oder verpflichtet sind, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

    <h2>Haftung für Inhalte dieser Website</h2>
    <p>Wir entwickeln die Inhalte dieser Website ständig weiter und bemühen uns korrekte und aktuelle Informationen bereitzustellen. Leider können wir keine Haftung für die Korrektheit aller Inhalte auf dieser Website übernehmen, speziell für jene, die seitens Dritter bereitgestellt wurden.<br>
    Als Diensteanbieter sind wir nicht verpflichtet, die von Ihnen übermittelten oder gespeicherten Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.<br>
    Unsere Verpflichtungen zur Entfernung von Informationen oder zur Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen aufgrund von gerichtlichen oder behördlichen Anordnungen bleiben auch im Falle unserer Nichtverantwortlichkeit davon unberührt.<br>
    Sollten Ihnen problematische oder rechtswidrige Inhalte auffallen, bitte wir Sie uns umgehend zu kontaktieren, damit wir die rechtswidrigen Inhalte entfernen können. Sie finden die Kontaktdaten im Impressum.</p>

    <h2>Haftung für Links auf dieser Website</h2>
    <p>Unsere Website enthält Links zu anderen Websites für deren Inhalt wir nicht verantwortlich sind. Haftung für verlinkte Websites besteht für uns nicht, da wir keine Kenntnis rechtswidriger Tätigkeiten hatten und haben, uns solche Rechtswidrigkeiten auch bisher nicht aufgefallen sind und wir Links sofort entfernen würden, wenn uns Rechtswidrigkeiten bekannt werden.<br>
    Wenn Ihnen rechtswidrige Links auf unserer Website auffallen, bitte wir Sie uns zu kontaktieren. Sie finden die Kontaktdaten im Impressum.</p>

    <h2>Urheberrechtshinweis</h2>
    <p>Alle Inhalte dieser Webseite (Bilder, Fotos, Texte, Videos) unterliegen dem Urheberrecht. Bitte fragen Sie uns bevor Sie die Inhalte dieser Website verbreiten, vervielfältigen oder verwerten wie zum Beispiel auf anderen Websites erneut veröffentlichen. Falls notwendig, werden wir die unerlaubte Nutzung von Teilen der Inhalte unserer Seite rechtlich verfolgen.<br>
    Sollten Sie auf dieser Webseite Inhalte finden, die das Urheberrecht verletzen, bitten wir Sie uns zu kontaktieren.</p>

    <h2>Bildernachweis</h2>
    <p>Die Bilder, Fotos und Grafiken auf dieser Webseite sind urheberrechtlich geschützt. Die Verwertungsrechte liegen bei: [Firmenname, Name der Person]</p>
    <p>[Bildnachweis], [Bildnachweis], [Bildnachweis]</p>
    <p>Alle Texte sind urheberrechtlich geschützt.</p>
"""

datenschutz_body = """
    <h1>Datenschutzerklärung</h1>

    <p>Nach Art 13 und 14 der Verordnung (EU) 2016/679 (Datenschutzgrundverordnung; „DSGVO“) muss der Verantwortliche den Betroffenen über die Verarbeitung personenbezogener Daten informieren. Mit diesem Dokument informieren wir Sie über die verarbeiteten personenbezogenen Daten.</p>

    <h2>Definitionen</h2>
    <p>Zur besseren Verständlichkeit dieser Datenschutzerklärung finden Sie im Folgenden eine kurze Erklärung der verwendeten Begriffe.</p>
    <p><strong>Personenbezogene Daten („Daten“)</strong> sind alle Daten, die Informationen über persönliche oder sachliche Verhältnisse natürlicher Personen enthalten, beispielsweise Name, Anschrift, Emailadresse, Telefonnummer, Geburtsdatum, Alter, Geschlecht, Sozialversicherungsnummer, Videoaufzeichnungen, Fotos etc. Daten von juristischen Personen unterliegen nicht den Bestimmungen der DSGVO.</p>
    <p><strong>Verarbeitung</strong> ist jeder mit oder ohne Hilfe automatisierter Verfahren ausgeführter Vorgang oder jede solche Vorgangsreihe im Zusammenhang mit personenbezogenen Daten wie das Erheben, das Erfassen, die Organisation, das Ordnen, die Speicherung, die Anpassung oder Veränderung, das Auslesen, das Abfragen, die Verwendung, die Offenlegung durch Übermittlung, Verbreitung oder eine andere Form der Bereitstellung, den Abgleich oder die Verknüpfung, die Einschränkung, das Löschen oder die Vernichtung.</p>
    <p><strong>Verantwortlicher</strong> ist die natürliche oder juristische Person, Behörde, Einrichtung oder andere Stelle, die allein oder gemeinsam mit anderen über die Zwecke und Mittel der Verarbeitung von personenbezogenen Daten entscheidet.</p>
    <p><strong>Auftragsverarbeiter</strong> ist eine natürliche oder juristische Person, Behörde, Einrichtung oder andere Stelle, die personenbezogene Daten im Auftrag des Verantwortlichen verarbeitet.</p>
    <p><strong>Empfänger</strong> ist eine natürliche oder juristische Person, Behörde, Einrichtung oder andere Stelle, der personenbezogene Daten offengelegt werden, unabhängig davon, ob es sich bei ihr um einen Dritten handelt oder nicht.</p>

    <h2>Unsere Kontaktdaten</h2>
    <p>Für den Fall, dass Sie weitere Fragen haben, stehen wir Ihnen, als Verantwortlicher der hierin behandelten Datenverarbeitung, unter folgenden Kontaktdaten gerne zur Verfügung:</p>
    <p>[Firmenname, Name der Person]<br>
    [Adresse, PLZ, Ort]<br>
    [Telefonnummer, Email Adresse]</p>

    <h2>Zwecke und Rechtsgrundlage der Verarbeitung</h2>
    <p>Daten dürfen nur zu einem bestimmten Zweck verarbeitet werden und nur, wenn sich die Verarbeitung auf eine entsprechende Rechtsgrundlage stützen kann. Die Verarbeitung kann aus folgenden Gründen gerechtfertigt sein:</p>
    <table>
        <tr><th>Rechtsfertigungstatbestand</th><th>Rechtsgrundlage</th></tr>
        <tr><td>aufgrund Ihrer freiwilligen Einwilligung zu einem bestimmten Zweck</td><td>Art 6 Abs 1 lit a</td></tr>
        <tr><td>zur Vertragserfüllung, sofern Sie Vertragspartner sind oder zur Anbahnung eines Vertragsschlusses, wenn die Verarbeitung auf Ihre Anfrage zurückgeht</td><td>Art 6 Abs 1 lit b</td></tr>
        <tr><td>aufgrund einer rechtlichen Verpflichtung, der wir unterliegen</td><td>Art 6 Abs 1 lit c</td></tr>
        <tr><td>zum Schutz Ihrer lebenswichtigen Interessen oder zum Schutz dieser Interessen einer anderen Person</td><td>Art 6 Abs 1 lit d</td></tr>
        <tr><td>zur Wahrnehmung einer Aufgabe im öffentlichen Interesse oder in Ausübung öffentlicher Gewalt, die uns übertragen wurde</td><td>Art 6 Abs 1 lit e</td></tr>
        <tr><td>auf Grundlage einer Interessenabwägung zwischen unserem Interesse oder dem Interesse eines Dritten an der Verarbeitung einerseits und Ihrem Interesse oder Ihren Grundrechten und Grundfreiheiten</td><td>Art 6 Abs 1 lit f</td></tr>
    </table>

    <p>Wir verarbeiten Ihre Daten zu den folgenden Zwecken auf Grundlage der folgenden Rechtsgrundlagen:</p>
    <table>
        <tr><th>Erfasste Datenkategorien</th><th>Zweck der Verarbeitung</th><th>Rechtsgrundlage</th></tr>
        <tr><td><strong>Kontaktdaten</strong><br>(Name, Adresse, E-Mail-Adresse, Telefonnummer)</td><td>Diese Daten sind zur Nutzung unseres Angebots bzw. zur Vertragsanbahnung notwendig und werden bei einer Kontaktaufnahme von Ihnen erhoben.</td><td>Art 6 Abs 1 lit a und b DSGVO</td></tr>
        <tr><td><strong>Technische Informationen</strong><br>(IP-Adresse, Betriebssystem)</td><td>Diese Daten sind erforderlich, damit Ihnen die über Ihre Initiative geöffnete Website in der korrekten Form angezeigt werden kann.</td><td>Art 6 Abs 1 lit f DSGVO</td></tr>
    </table>

    <h2>Empfänger</h2>
    <p>Empfänger unterstützen uns bei der Einhaltung gesetzlicher oder rechtlichen Pflichten, bei der Vertragsanbahnung und der Vertragserfüllung, bei Diensten, die Ihre Einwilligung voraussetzen oder bei der Wahrnehmung von Verarbeitungen, die in unserem berechtigten Interesse liegen. Wir übermitteln oder legen die Daten teilweise insbesondere folgenden Empfängern (Auftragsverarbeitern oder Verantwortliche) offen:</p>
    <table>
        <tr><th>Empfänger</th><th>Beschreibung</th></tr>
        <tr><td>IT-Dienstleister</td><td>Betrieb unseres IT-Systems, insbesondere E-Mail-Dienste, Hostingservices etc.</td></tr>
    </table>
    <p>An andere Empfänger übermitteln wir Ihre Daten nur, wenn Sie hierzu Ihre ausdrückliche Einwilligung nach Art 6 Abs 1 lit a DSGVO erteilt haben, dies gesetzlich zulässig und nach Art. 6 Abs 1 lit. b DSGVO zur Erfüllung eines Vertragsverhältnisses mit Ihnen erforderlich ist, oder wenn uns nach Art 6 Abs 1 lit c DSGVO eine gesetzliche Verpflichtung dazu trifft, oder die Weitergabe nach Art 6 Abs 1 lit f DSGVO zur Wahrung unserer berechtigten Interessen sowie zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen erforderlich ist und kein Grund zur Annahme besteht, dass Sie ein überwiegendes schutzwürdiges Interesse an der Nichtweitergabe Ihrer Daten haben.</p>

    <h2>Speicherdauer</h2>
    <p>Die Speicherung von Daten erfolgt grundsätzlich nur so lange, wie dies aufgrund gesetzlicher Aufbewahrungspflichten erforderlich ist. Darüber hinaus kann eine Speicherung erfolgen, wenn dies zur Durchsetzung oder Abwehr von Ansprüchen Dritter erforderlich ist. Wichtige Speicherfristen finden Sie im Folgenden:</p>
    <table>
        <tr><th>Pflicht zur Aufbewahrung</th><th>Voraussichtliche Speicherdauer</th></tr>
        <tr><td>Unternehmensrechtliche Aufbewahrungspflicht nach §§ 190, 212 UGB</td><td>7 Jahre</td></tr>
        <tr><td>Umsatzsteuerrechtliche Aufbewahrungspflicht für Rechnungen nach § 11 Abs 2 3. Unterabsatz UStG</td><td>7 Jahre</td></tr>
        <tr><td>Allgemeiner Schadenersatz nach § 1489 ABGB (Entschädigungsklagen)</td><td>3 Jahre/30 Jahre</td></tr>
    </table>

    <h2>Webhosting und Drittanbieter</h2>
    
    <h3>Domain Discount 24</h3>
    <p>Das Domain-Hosting für unsere Website wird von Domain Discount 24 (Key-Systems GmbH) bereitgestellt. Dienstanbieter ist die Key-Systems GmbH, Kaiserstraße 172-174, 66133 Saarbrücken, Deutschland.<br>
    Weitere Informationen zu den verarbeiteten Daten und dem Datenschutz bei Domain Discount 24 finden Sie in deren Datenschutzerklärung.</p>

    <h3>Vercel</h3>
    <p>Für das Hosting und die Bereitstellung unserer Website nutzen wir die Cloud-Plattform Vercel. Anbieter ist die Vercel Inc., 340 S Lemon Ave #4133, Walnut, CA 91789, USA (im Folgenden: Vercel).</p>
    <ul>
        <li><strong>Art der Daten:</strong> IP-Adresse, Request-Header und Log-Daten.</li>
        <li><strong>Zweck:</strong> Schnelle Auslieferung der Website über ein globales Netzwerk (CDN) und Absicherung gegen DDoS-Angriffe.</li>
        <li><strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. f DSGVO (Berechtigtes Interesse an einer performanten und sicheren Web-Infrastruktur).</li>
        <li><strong>Datenübertragung:</strong> Vercel ist unter dem EU-U.S. Data Privacy Framework zertifiziert. Die Übermittlung in die USA erfolgt somit auf Grundlage eines Angemessenheitsbeschlusses der EU-Kommission.</li>
        <li><strong>Weitere Informationen:</strong> Weitere Details finden Sie in der Datenschutzerklärung von Vercel.</li>
    </ul>

    <h2>Rechtsbelehrung</h2>
    <h3>Auskunftsrecht</h3>
    <p>Sie haben das Recht eine Bestätigung darüber zu verlangen, ob personenbezogene Daten verarbeitet werden; ist dies der Fall, so haben Sie ein Recht auf Auskunft über diese personenbezogenen Daten.</p>

    <h3>Recht auf Berichtigung</h3>
    <p>Sie haben das Recht, von dem Verantwortlichen die Berichtigung unrichtiger sowie die Vervollständigung unvollständiger personenbezogener Daten zu verlangen.</p>

    <h3>Recht auf Löschung</h3>
    <p>Sie haben das Recht, von dem Verantwortlichen zu verlangen, dass personenbezogene Daten unverzüglich gelöscht werden, sofern die personenbezogenen Daten für die Zwecke, für die sie erhoben wurden, nicht mehr notwendig sind oder eine andere der gesetzlichen Voraussetzungen zutrifft.</p>

    <h3>Recht auf Einschränkung der Verarbeitung</h3>
    <p>Sie haben das Recht die Einschränkung der Verarbeitung zu verlangen, wenn die Richtigkeit der personenbezogenen Daten bestritten wird oder eine andere der gesetzlichen Voraussetzungen zutrifft.</p>

    <h3>Recht auf Datenübertragbarkeit</h3>
    <p>Sie haben das Recht, die personenbezogenen Daten, die Sie einem Verantwortlichen bereitgestellt haben, in einem strukturierten, gängigen und maschinenlesbaren Format zu erhalten.</p>

    <h3>Widerspruchsrecht</h3>
    <p>Sie haben das Recht, aus Gründen, die sich aus Ihrer besonderen Situation ergeben, jederzeit gegen die Verarbeitung personenbezogener Daten Widerspruch einzulegen.</p>

    <h3>Recht auf Widerruf der Einwilligung</h3>
    <p>Sie haben das Recht, eine Einwilligung jederzeit zu widerrufen, ohne dass die Rechtsmäßigkeit der Verarbeitung bis zum Widerruf berührt wird.</p>

    <h3>Beschwerderecht</h3>
    <p>Sie haben das Recht auf Beschwerde bei der Österreichischen Datenschutzbehörde, Barichgasse 40-42, 1030 Wien, T.: 00431521522569, E.: dsb@gsb.gv.at, wenn Sie der Auffassung sind, dass die Verarbeitung gegen das geltende Datenschutzrecht verstößt.</p>
"""

footer_html = """
  </div>
</body>
</html>
"""

with open("impressum.html", "w") as f:
    f.write(head_content.replace("<title>AUF Tirol – Aktiv und Fit Tirol</title>", "<title>Impressum – AUF Tirol</title>") + extra_styles + impressum_body + footer_html)

with open("datenschutz.html", "w") as f:
    f.write(head_content.replace("<title>AUF Tirol – Aktiv und Fit Tirol</title>", "<title>Datenschutz – AUF Tirol</title>") + extra_styles + datenschutz_body + footer_html)

