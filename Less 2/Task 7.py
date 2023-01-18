tool = 'Super-Puper MainTool /v2*'
super_tool = tool[:5] + tool[16:21] + tool[-3:-1].replace('2', '1')

print('*********************\n', super_tool.center(20, '-'),
      '\n*********************')
