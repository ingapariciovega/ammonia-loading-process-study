"""Straight-pipe geometry only; no fluid-property or safety prediction."""
from pathlib import Path
import json, math

def calculate(data):
    density=data['assumed_density_kg_m3']
    if not math.isfinite(density) or density<=0:
        raise ValueError('Density must be positive and finite.')
    sections=[]
    for s in data['sections']:
        d,L,n=s['internal_diameter_m'],s['length_per_line_m'],s['number_of_lines']
        if not all(math.isfinite(v) and v>0 for v in [d,L,n]) or int(n)!=n:
            raise ValueError('Positive dimensions and an integer line count are required.')
        v=math.pi*d*d*L*n/4
        sections.append({'id':s['id'],'volume_m3':v,'hypothetical_inventory_kg':v*density})
    return {'sections':sections,'total_volume_m3':sum(s['volume_m3'] for s in sections),'hypothetical_inventory_kg':sum(s['hypothetical_inventory_kg'] for s in sections),'density_basis':'Supplied assumption; no thermodynamic state verified.'}

if __name__=='__main__':
    result=calculate(json.loads(Path(__file__).with_name('example-input.json').read_text()))
    print(json.dumps(result,indent=2))
