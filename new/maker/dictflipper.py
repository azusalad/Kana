#version 20210428 made it print at the end
import wx
import ast
import re
def get_path(wildcard):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path

print('Choose a dictionary')
file_path = get_path('*.txt')
f = open(file_path, "r")
file_index = f.read().split("\n")
#print(f.name)
f.close()
old_dict = ast.literal_eval(file_index[0])
flipped_dict = {}
for x in old_dict:
    flipped_dict[str(old_dict[x])] = [x]  # swaps keys and values
#new_path = re.sub(r"^.+\\(.+)\.txt$", r"\1" + ' flipped.txt', file_path)
new_path = re.sub(r"^(.+\/.+)\.txt$", r"\1" + ' flipped.txt', file_path)
# change to re.sub(r"^(.+\\.+)\.txt$", r"\1" + ' flipped.txt', file_path) if you use windows
f = open(new_path, 'w')
#print(new_path)
f.write(str(flipped_dict))
f.close()
print('Created a flipped dictionary at file location:\n' + str(new_path))
