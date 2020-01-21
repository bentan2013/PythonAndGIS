import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.colors as colors

def generate_data(idx=[0,1,2,3,4,5]):
    date = ["Jan.19", "Jan.20", "Jan.21", "Jan.22", "Jan.23",
            "Jan.24", "Jan.25", "Jan.26", "Jan.27", "Jan.28", 
            "Jan.29", "Jan.30", "Jan.31", "Feb.01", "Feb.02", 
            "Feb.03", "Feb.04", "Feb.05"]

    name = ["James", "Mary", "Ben", "John", "Linda", "Tonny"]
    name = np.array(name)

    # 0: office
    # 1: remote
    # 2: vacation
    # 3: public holiday
    # 4: half day

    # start from Jan.19, end with Feb.05
    teams = np.zeros([len(name), len(date)])
    legal_holiday  = [0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 0, 0, 0]
    teams += legal_holiday
    #                19              24                   31             5
    # James 
    teams[0]      += [1, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0]
    # Mary
    teams[1]      += [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0]
    # Ben
    teams[2]      += [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0]
    # John
    teams[3]      += [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 2]
    # Linda 
    teams[4]      += [0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0]
    # Tonny
    teams[5]      += [0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 4]

    # filter by idx
    teams_new = np.zeros([len(idx), len(date)])
    name_new = np.zeros(len(idx),)

    teams_new = teams[idx]
    name_new = name[idx]
    return teams_new, date, name_new



member_index = [0, 1, 5, 5, 5]
teams, date, name = generate_data(member_index)

 # 0: office
 # 1: remote
 # 2: vacation
 # 3: public holiday
 # 4: half day

# figure
color_list = ['darkblue', 'skyblue', 'yellow', 'darkred', 'lightgreen']
self_cmap = colors.ListedColormap(color_list)
fig = plt.figure()
ax = fig.add_subplot(111)
h = ax.imshow(teams, cmap=self_cmap)

# legend
label_list = ['Half day off', 'Public Holiday', 'Vacation',  'Remote', 'Office']
handles = []
for i in range(len(color_list)):
    handles.append(mpatches.Patch(color=color_list[i], label=label_list[len(color_list) - i - 1]))

plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0., handles=handles)

# emoji annotation 
emojis = ['😱', '😂', '😊',  '😄', '😛']
for i in range(len(name)):
    for j in range(len(date)):
        ann = emojis[int(teams[i, j])]
        color = 'w'
        if int(teams[i, j]) in [1, 2, 4]: 
            color = 'b'
        text = ax.text(j, i, ann, ha='center', va='center', color=color, fontsize='16')

# axis 
ax.set_xticks(np.arange(0, len(date), 1))
ax.set_yticks(np.arange(0, len(name), 1))
ax.set_xticklabels(date)
ax.set_yticklabels(name)
ax.set_xticks(np.arange(-.5, len(date), 1), minor=True)
ax.set_yticks(np.arange(-.5, len(name), 1), minor=True)
ax.xaxis.set_ticks_position('bottom')
plt.xticks(rotation=60)

# grid
ax.grid(color='w', which='minor', linestyle='-', linewidth=2)

# title
plt.title('Spring Festival holiday for Dev Team', fontsize=20)
plt.show()
