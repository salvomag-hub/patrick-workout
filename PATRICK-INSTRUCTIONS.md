# Come Patrick può inviare workout a Elisa

## Formato Workout
Il workout è un JSON con questa struttura:
```json
{
  "name": "Nome del Workout",
  "exercises": [
    {
      "name": "Nome Esercizio",
      "description": "Come eseguire l'esercizio",
      "type": "timer",      // oppure "reps"
      "duration": 30,       // secondi (se type=timer)
      "reps": 10,           // ripetizioni (se type=reps)
      "rest": 15            // secondi di recupero
    }
  ]
}
```

## Generare il Codice
Il codice è semplicemente il JSON convertito in base64:
```python
import json, base64

workout = {
    "name": "Full Body di Patrick",
    "exercises": [
        {"name": "Jumping Jacks", "description": "Salta aprendo braccia e gambe", "type": "timer", "duration": 30, "rest": 15},
        {"name": "Squat", "description": "Piedi larghezza spalle, scendi fino a cosce parallele", "type": "reps", "reps": 15, "rest": 20},
        # ... altri esercizi
    ]
}

code = base64.b64encode(json.dumps(workout).encode()).decode()
print(code)
```

## Inviare a Elisa
1. Genera il codice base64 del workout
2. Manda a Elisa un messaggio tipo:

"Ecco il tuo workout! 💪
Apri l'app Patrick Workout → 📥 Import → incolla questo codice:

[CODICE BASE64]"

Oppure usa il link diretto:
https://[URL-APP]/?w=[CODICE BASE64]

## Script Helper
```bash
python3 /root/clawd/apps/workout-app/generate_workout.py "Nome Workout" << 'EOF'
Jumping Jacks|Salta aprendo braccia e gambe|timer|30|15
Squat|Piedi larghezza spalle|reps|15|20
Plank|Mantieni la posizione|timer|45|15
EOF
```
