# Detta är en väldigt missvisande uträkning, den visar att den har rätt 98.7% av gångerna men då majoriteten av dom är true negeative (ingen eld) så ser det,
# ut att ha rätt ofta men det är missvisande då den bara korrekt fångar upp 2 av 13 riktiga bränder vilket blir låga 15%. 
import math

tp = 2
fp = 2
fn = 11
tn = 985
accuracy = (tp + tn) / (tp + tn + fp + fn)
result = accuracy * 100
print(f"{result}%")