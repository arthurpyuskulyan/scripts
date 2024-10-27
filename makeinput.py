# works Content for gs.com
gs_com_content = """%chk=gs.chk
# freq=(savenm,hpmodes) cam-b3lyp/6-31G* Charge nosymm 

 gs

0	1
"""

# Write the content to gs.com
with open("gs.com", "w") as gs_com_file:
    gs_com_file.write(gs_com_content)

# Read the contents of qmmm.xyz excluding the first two lines
with open("qmmm.xyz", "r") as qmmm_file:
    qmmm_lines = qmmm_file.readlines()[2:]

# Append the modified contents of qmmm.xyz to gs.com
with open("gs.com", "a") as gs_com_file:
    gs_com_file.writelines(qmmm_lines)


# works  Content for es.com
es_com_content = """%chk=es.chk
# cam-b3lyp/6-31G* TDA(Root=1) freq=(savenm,hpmodes) Charge nosymm 

 es

0	1
"""

# Write the content to gs.com
with open("es.com", "w") as es_com_file:
    es_com_file.write(es_com_content)

# Read the contents of qmmm.xyz excluding the first two lines
with open("qmmm.xyz", "r") as qmmm_file:
    qmmm_lines = qmmm_file.readlines()[2:]

# Append the modified contents of qmmm.xyz to es.com
with open("es.com", "a") as es_com_file:
    es_com_file.writelines(qmmm_lines)

    
