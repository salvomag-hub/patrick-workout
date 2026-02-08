#!/usr/bin/env python3
"""
Generate workout code for Patrick Workout App

Usage:
    python3 generate_workout.py "Workout Name" << 'EOF'
    Exercise Name|Description|type|duration_or_reps|rest
    Jumping Jacks|Jump opening arms and legs|timer|30|15
    Squat|Feet shoulder width|reps|15|20
    EOF

Or call from Python:
    from generate_workout import create_workout_code
    code = create_workout_code("My Workout", exercises)
"""

import json
import base64
import sys

def create_workout_code(name: str, exercises: list) -> str:
    """Create a base64 encoded workout code."""
    workout = {
        "name": name,
        "exercises": exercises
    }
    return base64.b64encode(json.dumps(workout).encode()).decode()

def parse_exercise_line(line: str) -> dict:
    """Parse a pipe-separated exercise line."""
    parts = line.strip().split('|')
    if len(parts) < 5:
        raise ValueError(f"Invalid line: {line}")
    
    ex = {
        "name": parts[0],
        "description": parts[1],
        "type": parts[2],
        "rest": int(parts[4])
    }
    
    if parts[2] == "timer":
        ex["duration"] = int(parts[3])
        ex["reps"] = 10  # default
    else:
        ex["reps"] = int(parts[3])
        ex["duration"] = 30  # default
    
    return ex

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_workout.py 'Workout Name'")
        print("Then pipe exercises in format: Name|Description|type|value|rest")
        sys.exit(1)
    
    workout_name = sys.argv[1]
    exercises = []
    
    print(f"Enter exercises (Name|Description|type|duration_or_reps|rest):")
    print("Press Ctrl+D when done.")
    print()
    
    for line in sys.stdin:
        line = line.strip()
        if line:
            try:
                exercises.append(parse_exercise_line(line))
            except ValueError as e:
                print(f"Warning: {e}", file=sys.stderr)
    
    if not exercises:
        print("No exercises provided!", file=sys.stderr)
        sys.exit(1)
    
    code = create_workout_code(workout_name, exercises)
    
    print()
    print("=" * 60)
    print(f"Workout: {workout_name}")
    print(f"Exercises: {len(exercises)}")
    print("=" * 60)
    print()
    print("📋 CODICE DA INVIARE A ELISA:")
    print()
    print(code)
    print()
    print("=" * 60)

if __name__ == "__main__":
    main()
