import json

def audit_synthesis_queue(input_path, output_path):
    with open(input_path, 'r') as f:
        fragments = json.load(f)

    flagged = []
    for frag in fragments:
        missing_fields = []
        for field in ['bias_score', 'drift_score', 'contradiction_score', 'tags']:
            if field not in frag or frag[field] in [None, '', [], {}]:
                missing_fields.append(field)
        if missing_fields:
            flagged.append({
                'id': frag.get('id', 'unknown'),
                'missing_fields': missing_fields,
                'content': frag.get('content', '[no content]')
            })

    with open(output_path, 'w') as f:
        json.dump(flagged, f, indent=2)

    print(f"Audit complete. {len(flagged)} fragments flagged.")

# Example usage:
audit_synthesis_queue('synthesis_queue.json', 'logging_integrity_report.json')

