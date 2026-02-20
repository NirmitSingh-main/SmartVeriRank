import os
import re
import csv

# Resolve project paths relative to this file (ml/src/parser/.. -> ml)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
SIM_DIR = os.path.join(BASE_DIR, "sim")
OUT_FILE = os.path.join(BASE_DIR, "data", "events.csv")


def parse_logs():
    rows = []

    for filename in os.listdir(SIM_DIR):
        if not filename.endswith(".log"):
            continue

        run_id = filename.replace(".log", "")
        filepath = os.path.join(SIM_DIR, filename)

        with open(filepath, "r") as f:
            lines = f.readlines()

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Detect ERROR or WARNING line
            if line.startswith("ERROR") or line.startswith("WARNING"):
                severity = "ERROR" if line.startswith("ERROR") else "WARNING"

                # Extract error type inside [ ... ]
                error_match = re.search(r"\[(.*?)\]", line)
                error_type = error_match.group(1) if error_match else "UNKNOWN"

                # Extract message (text after ])
                message = line.split("]")[-1].strip()

                # Next line contains simulation time
                sim_time = -1
                if i + 1 < len(lines):
                    time_match = re.search(r"Time:\s*(\d+)", lines[i + 1])
                    if time_match:
                        sim_time = int(time_match.group(1))

                rows.append([
                    run_id,
                    sim_time,
                    severity,
                    error_type,
                    message
                ])

                i += 2
            else:
                i += 1

    return rows


def write_csv(rows):
    with open(OUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "run_id",
            "time",
            "severity",
            "error_type",
            "message"
        ])
        writer.writerows(rows)


if __name__ == "__main__":
    events = parse_logs()
    write_csv(events)
    print(f"[OK] Parsed {len(events)} events into {OUT_FILE}")