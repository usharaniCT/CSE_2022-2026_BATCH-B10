def get_suggestions(result):

    suggestions = {

        "normal": """
STAGE 1: NORMAL (Early Detection)
The Prevention Phase" The infestation is in its initial stages, and the plant shows minimal to no visible damage.
1. Description & Signs
మొదటి దశ: ప్రారంభ దశ (ముందస్తు గుర్తింపు)

PLACES OF DAMAGE (ప్రభావిత ప్రాంతాలు):
English: Foundation bases, door frames, window sills, and skirting boards.
తెలుగు: ఇంటి పునాదులు, తలుపుల గడపలు, కిటికీ ఫ్రేములు మరియు గోడ మూలలు.

CAUSE OF DAMAGE (కారణాలు):
English: Cracks in the foundation, high moisture levels, and wood directly touching damp soil.
తెలుగు: పునాదులలో పగుళ్లు, గదిలో తేమ ఎక్కువగా ఉండటం మరియు చెక్క నేరుగా తడి నేలను తాకడం.

PRECAUTIONS & ACTION (జాగ్రత్తలు మరియు నివారణ):
English: Seal all cracks with waterproof cement. Keep the area around walls dry. Apply Neem oil spray to the edges once a week.
తెలుగు: గోడల పగుళ్లను వాటర్‌ప్రూఫ్ సిమెంట్‌తో పూడ్చాలి. గోడల చుట్టూ తడి లేకుండా చూడాలి. వారానికి ఒకసారి వేప నూనెను గోడల వెంట చల్లాలి.
""",

        "moderate": """
STAGE 2: MODERATE DAMAGE
రెండవ దశ: మధ్యస్థ దశ (నష్టం మొదలైన సమయం)

PLACES OF DAMAGE (ప్రభావిత ప్రాంతాలు):
English: Inside wardrobes, plywood partitions, and behind heavy furniture or wall-mounted units.
తెలుగు: బీరువాల లోపల, ప్లైవుడ్ పార్టిషన్లు, బరువుగా ఉండే ఫర్నిచర్ వెనుక భాగాలు.

CAUSE OF DAMAGE (కారణాలు):
English: Lack of air ventilation, trapped humidity behind walls, and storing cardboard boxes near wood.
తెలుగు: గాలి వెలుతురు సరిగ్గా లేకపోవడం, గోడల వెనుక తేమ పేరుకుపోవడం మరియు అట్టపెట్టెలను చెక్క సామాగ్రి దగ్గర ఉంచడం.

PRECAUTIONS & ACTION (జాగ్రత్తలు మరియు నివారణ):
English: Inject Termiticide (Fipronil) or Boric Acid into small drill holes. Expose movable furniture to direct sunlight for 3-4 days.
తెలుగు: చిన్న రంధ్రాలు చేసి అందులోకి చెదల మందును ఇంజెక్ట్ చేయాలి. పాడైన సామాగ్రిని 3-4 రోజులు నేరుగా ఎండలో ఉంచాలి.
""",

        "severe": """
STAGE 3: SEVERE DAMAGE (Structural Risk)
మూడవ దశ: తీవ్ర దశ (నిర్మాణ ప్రమాదం)

PLACES OF DAMAGE (ప్రభావిత ప్రాంతాలు):
English: Main structural roof beams, support pillars, and fixed cabinetry/wardrobes.
తెలుగు: ఇంటి పైకప్పు దూలాలు (Beams), మెయిన్ స్తంభాలు మరియు గోడకు ఫిక్స్ చేసిన వార్డ్‌రోబ్‌లు.

CAUSE OF DAMAGE (కారణాలు):
English: Neglect of early signs, leading to subterranean colonies destroying the core of the wood.
తెలుగు: ప్రారంభంలో నిర్లక్ష్యం చేయడం వల్ల భూమిలోని చెద పుట్టలు ఇంటి ప్రధాన నిర్మాణాన్ని లోపల నుండి తినేయడం.

REPAIR OR REPLACE? (మార్చాలా లేదా బాగుచేయాలా?):
English: REPLACE IMMEDIATELY if the wood is a structural support or if more than 30% of the surface sounds hollow. The wood has lost its strength and is unsafe.
తెలుగు: వెంటనే మార్చాలి - ఒకవేళ అది పునాది దూలం (Support beam) అయినా లేదా 30% కంటే ఎక్కువ దొల్లగా (Hollow) మారినా ఆ సామాగ్రిని వెంటనే మార్చాలి.

EMERGENCY PRECAUTIONS (అత్యవసర జాగ్రత్తలు):
English: Remove and burn infested wood. Perform a professional "Soil Treatment" around the+ foundation using Imidacloprid.
తెలుగు: పాడైన చెక్కను తీసి వెంటనే కాల్చివేయాలి. ఇంటి పునాది చుట్టూ భూమిలోకి మందును పంపించే 'సాయిల్ ట్రీట్మెంట్' చేయించాలి.

FINAL SAFETY CHECKLIST / ముగింపు జాగ్రత్తలు:
Never let wood touch damp soil. (చెక్కను తడి నేలపై ఉంచకండి).
Fix water leaks immediately. (లీకేజీలను వెంటనే బాగు చేయండి).
Do not store cardboard or old books against walls. (అట్టపెట్టెలను గోడలకు ఆనించి ఉంచకండి).
Ensure sunlight and air in dark corners. (చీకటి గదుల్లో గాలి, వెలుతురు ఉండేలా చూడండి).
"""
    }

    return suggestions.get(result.lower(), "No suggestions available.")