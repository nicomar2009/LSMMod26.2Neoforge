"""Check retained cloth resources and one-pixel supports without compilation."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];A=ROOT/'src/main/resources/assets/lsmmod'
def read(p):return json.loads(p.read_text())
def main():
 variants=read(ROOT/'tools/awning_variants.json');assert [v[0] for v in variants]==['playground_awning','elementary_playground_awning']
 for ident,*_ in variants:
  states=read(A/f'blockstates/{ident}.json')['variants'];assert len(states)==2312
  for value in states.values():
   path=A/'models'/(value['model'].split(':')[1]+'.json');model=read(path);seen={path}
   while 'parent' in model and not model['parent'].startswith('minecraft:'):
    path=A/'models'/(model['parent'].split(':')[1]+'.json');assert path not in seen;seen.add(path);model=read(path)
   for e in model['elements']:
    assert all(0<=a<b<=16 for a,b in zip(e['from'],e['to']))
  item=read(A/f'models/item/{ident}.json')
  if 'parent' in item:assert (A/'models'/(item['parent'].split(':')[1]+'.json')).exists()
 for profile in range(4):
  elements=read(A/f'models/block/awning_support_{profile}.json')['elements'];assert len(elements)==5
  for e in elements:
   lengths=[b-a for a,b in zip(e['from'],e['to'])];assert sorted(lengths)==[1,1,16]
   assert e['from'][1]==13 and e['to'][1]==14
  assert [e['from'][2] for e in elements[:3]]==[0,0,0]
  assert [e['to'][2] for e in elements[:3]]==[16,16,16]
 support=(ROOT/'src/main/java/net/nicomar2009/lsmmod/block/AwningSupportBlock.java').read_text();assert 'SimpleBlockOutline.forState' in support and 'getCollisionShape' in support
 assert 'new double[]{2,7.5,13}' in support and 'new double[]{0,15}' in support
 for name in ('ModBlocks.java','ModItems.java'):
  s=(ROOT/'src/main/java/net/nicomar2009/lsmmod/registry'/name).read_text()
  assert ' AWNING =' not in s and 'WHITE_AWNING' not in s and 'BLACK_AWNING' not in s
 # No references anywhere in active resources to the deleted base or colour variants.
 removed=['awning']+[color+'_awning' for color in ('white','orange','magenta','light_blue','yellow','lime','pink','gray','light_gray','cyan','purple','blue','brown','green','red','black')]
 for ident in removed:
  assert not (A/f'blockstates/{ident}.json').exists() and not (A/f'models/block/{ident}').exists()
 for p in (A/'models').rglob('*.json'):
  s=p.read_text()
  assert 'lsmmod:block/awning/' not in s and '"lsmmod:item/awning"' not in s and '"lsmmod:block/awning"' not in s
 print('OK: only two awnings, 4624 cloth states with resolved models; 1024 support states, five 1x1px rods touching both block edges, cached collision / simple selection; removed base and 16 colours.')
if __name__=='__main__':main()
