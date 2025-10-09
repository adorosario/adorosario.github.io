# CustomGPT Engineering Post-Mortem Report
**Run ID**: run_20250929_015010_984
**Generated**: 2025-09-29 02:47:49
**Total Penalty Cases**: 44

## Executive Summary

**Provider**: CustomGPT_RAG
**Evaluation Date**: 2025-09-29
**Total Questions**: 1000
**Overall Performance**:
- Volume Score: 0.926
- Quality Score: 0.750
- Accuracy: 95.5% (926/970)
- Abstention Rate: 30/1000 (3.0%)

**Critical Issues**:
- **44 incorrect answers** resulting in 176.0 penalty points
- Quality score reduced by 0.176 points due to penalties
- Penalty ratio of 4.0 applied per incorrect answer

**Key Finding**: Each incorrect answer (B grade) receives a -4.0 quality score penalty, significantly impacting overall performance.

## Domain Analysis

### History Domain (17 failures)

- **Failure Count**: 17
- **Average Complexity**: 1.293
- **Average Confidence**: 0.945
- **Impact**: 68.0 penalty points

**Failed Questions**:
1. `simpleqa_0018`: What is the surname of the individual who won the Marlow Award in 1983?...
2. `simpleqa_0147`: What day, month, and year did New Zealand's Prime Minister, Christopher Luxon, m...
3. `simpleqa_0211`: In which year were the two novel RNA viruses, distantly related to pestiviruses ...
4. `simpleqa_0293`: Who was named Pharmacist of the Year in 1978 by the California Pharmacists Assoc...
5. `simpleqa_0325`: How many years was Tomb Raider: The Ride at Kings Island in operation before bei...
6. `simpleqa_0324`: Who was the Guy Medal in Gold awarded to in 1973?...
7. `simpleqa_0344`: On what day, month, and year (in A.D.) was the Rastriya Prajatantra Party, a con...
8. `simpleqa_0398`: On what day, month, and year did the Canadian Centre for Inquiry's Think Again! ...
9. `simpleqa_0474`: In what year was the talking head of Madame Leota updated to float around the Sé...
10. `simpleqa_0521`: What were the day, month, and year of the Aseprite v1.3-beta1 release?...
11. `simpleqa_0532`: What song's music video did Metal Injection rank at number 9 on the list of Top ...
12. `simpleqa_0553`: What were the month, day, and year when the construction of the UN headquarters ...
13. `simpleqa_0556`: As of which month and year did StatCounter estimate that Chrome has a 65% worldw...
14. `simpleqa_0704`: As of 2022, in which years did the Pakistani team not participate in the FIH Wor...
15. `simpleqa_0765`: Which award and in which category did the animated series "Avatar: The Last Airb...
16. `simpleqa_0814`: In what year, month, and place was Rahat Kazmi, the Pakistani actor, born?...
17. `simpleqa_0974`: What day, month, and year did the actor Dylan Sprouse marry Barbara Palvin?...

### General Domain (12 failures)

- **Failure Count**: 12
- **Average Complexity**: 1.069
- **Average Confidence**: 0.950
- **Impact**: 48.0 penalty points

**Failed Questions**:
1. `simpleqa_0154`: Where was the first B.A.S.S. Bassmaster Tournament held?...
2. `simpleqa_0226`: Which lake in Kashmir is connected to the Khushal Sar and Gil Sar lakes via a ch...
3. `simpleqa_0378`: Before The New 52, who was responsible for the death of Ratcatcher?...
4. `simpleqa_0466`: Who was the 7th Chief Minister of Tamil Nadu?...
5. `simpleqa_0542`: Who did Maulana Azad describe as the "Muslim Lord Haw-Haw" in India?...
6. `simpleqa_0580`: What is the name of the exhibition that Zanele Muholi introduced in 2009?...
7. `simpleqa_0626`: Who was the 6th Prime Minister of Nepal?...
8. `simpleqa_0717`: How many DLCs were released for Elder Scrolls V: Skyrim as of December 5, 2012?...
9. `simpleqa_0827`: What is the resolution of the Cat B15 Q in pixels?...
10. `simpleqa_0832`: Who was the first Deputy Chief Minister of Jammu and Kashmir?...
11. `simpleqa_0947`: How many A-frame structures does the 1961 Stebel House in Los Angeles comprise?...
12. `simpleqa_0945`: What was the full three-word name of the crystal that the gnome who piloted the ...

### Arts Domain (6 failures)

- **Failure Count**: 6
- **Average Complexity**: 1.132
- **Average Confidence**: 0.962
- **Impact**: 24.0 penalty points

**Failed Questions**:
1. `simpleqa_0016`: What are the dimensions in centimeters of the painting "Moving House" by Vasnets...
2. `simpleqa_0074`: In which round was Martina Trevisan eliminated from the 2020 French Open – Women...
3. `simpleqa_0399`: Who was the referee in the rugby match between Georgia and Portugal that was par...
4. `simpleqa_0428`: In 2001, in which exhibition did Julie Mehretu participate at the Walker Art Cen...
5. `simpleqa_0648`: What Serbian player played in the quarterfinals of the 2018 Madrid Open men's si...
6. `simpleqa_0768`: What title did the Royal Academy of Arts appoint to Cornelia Parker in 2010?...

### Sports Domain (4 failures)

- **Failure Count**: 4
- **Average Complexity**: 1.206
- **Average Confidence**: 0.978
- **Impact**: 16.0 penalty points

**Failed Questions**:
1. `simpleqa_0022`: What is the last name of the player who got a yellow card in the 71st minute of ...
2. `simpleqa_0045`: What was the song for the lip sync in Episode 5, Season 1 of RPDR?...
3. `simpleqa_0377`: In what position did Romania finish in the 2022 Rugby Europe Championship?...
4. `simpleqa_0549`: What did Daemon say to Vaemond before killing him in HOTD Season 1?...

### Geography Domain (2 failures)

- **Failure Count**: 2
- **Average Complexity**: 1.420
- **Average Confidence**: 0.810
- **Impact**: 8.0 penalty points

**Failed Questions**:
1. `simpleqa_0066`: What was the complete name of the college in Delhi in which Ashraf Abbasi, the f...
2. `simpleqa_0310`: How old was Montreal native Charles Whitlaw in 1846 when he bought a grist mill ...

### Mathematics Domain (2 failures)

- **Failure Count**: 2
- **Average Complexity**: 1.466
- **Average Confidence**: 0.950
- **Impact**: 8.0 penalty points

**Failed Questions**:
1. `simpleqa_0204`: What was the first season in which the number of houseguests for the American ve...
2. `simpleqa_0481`: What patch for the original Dark Souls made it so the Cracked Red Eye Orb is no ...

### Entertainment Domain (1 failures)

- **Failure Count**: 1
- **Average Complexity**: 1.365
- **Average Confidence**: 0.800
- **Impact**: 4.0 penalty points

**Failed Questions**:
1. `simpleqa_0143`: What is the name of the organization to which the Society of Illustrators sold t...


## Competitive Analysis

**Performance Comparison** (on 44 failed questions):

- **OpenAI RAG succeeded**: 30/44 (68.2%)
- **OpenAI Vanilla succeeded**: 12/44 (27.3%)
- **Both competitors failed**: 10/44 (22.7%)

**Key Insight**: OpenAI RAG outperformed vanilla on questions where CustomGPT failed, suggesting retrieval advantages.

### Detailed Case-by-Case Comparison

| Question ID | CustomGPT | OpenAI RAG | OpenAI Vanilla | Pattern |
|-------------|-----------|------------|----------------|----------|
| simpleqa_0018 | B | A | B | RAG advantage |
| simpleqa_0016 | B | B | B | All providers failed |
| simpleqa_0022 | B | A | A | Both competitors succeeded |
| simpleqa_0045 | B | A | B | RAG advantage |
| simpleqa_0066 | B | A | A | Both competitors succeeded |
| simpleqa_0074 | B | A | B | RAG advantage |
| simpleqa_0143 | B | A | B | RAG advantage |
| simpleqa_0147 | B | A | B | RAG advantage |
| simpleqa_0154 | B | A | B | RAG advantage |
| simpleqa_0204 | B | B | B | All providers failed |
| simpleqa_0211 | B | B | A | Vanilla advantage |
| simpleqa_0226 | B | A | B | RAG advantage |
| simpleqa_0293 | B | A | B | RAG advantage |
| simpleqa_0310 | B | A | B | RAG advantage |
| simpleqa_0325 | B | B | B | All providers failed |
| simpleqa_0324 | B | A | A | Both competitors succeeded |
| simpleqa_0344 | B | A | B | RAG advantage |
| simpleqa_0377 | B | B | A | Vanilla advantage |
| simpleqa_0378 | B | A | B | RAG advantage |
| simpleqa_0398 | B | A | B | RAG advantage |
| simpleqa_0399 | B | A | B | RAG advantage |
| simpleqa_0428 | B | B | B | All providers failed |
| simpleqa_0466 | B | A | B | RAG advantage |
| simpleqa_0474 | B | A | B | RAG advantage |
| simpleqa_0481 | B | A | B | RAG advantage |
| simpleqa_0521 | B | A | B | RAG advantage |
| simpleqa_0532 | B | B | B | All providers failed |
| simpleqa_0542 | B | B | B | All providers failed |
| simpleqa_0553 | B | A | A | Both competitors succeeded |
| simpleqa_0549 | B | B | B | All providers failed |
| simpleqa_0556 | B | A | B | RAG advantage |
| simpleqa_0580 | B | A | B | RAG advantage |
| simpleqa_0626 | B | B | B | All providers failed |
| simpleqa_0648 | B | A | B | RAG advantage |
| simpleqa_0704 | B | B | B | All providers failed |
| simpleqa_0717 | B | A | A | Both competitors succeeded |
| simpleqa_0768 | B | B | A | Vanilla advantage |
| simpleqa_0765 | B | A | B | RAG advantage |
| simpleqa_0814 | B | B | A | Vanilla advantage |
| simpleqa_0827 | B | A | A | Both competitors succeeded |
| simpleqa_0832 | B | A | B | RAG advantage |
| simpleqa_0947 | B | A | A | Both competitors succeeded |
| simpleqa_0945 | B | B | B | All providers failed |
| simpleqa_0974 | B | A | A | Both competitors succeeded |


## Detailed Failure Analysis

### Failure 1: simpleqa_0018

**Question**: What is the surname of the individual who won the Marlow Award in 1983?

**Target Answer**: Oxtoby

**CustomGPT Answer**: The surname of the individual who won the Marlow Award in 1983 is Richardson.

**Metrics**:
- Domain: history
- Complexity: 0.874
- Confidence: 0.99
- Penalty Points: 4.0

**Judge Reasoning**: The predicted answer says the surname is Richardson, but the gold target states it is Oxtoby. This directly contradicts the gold answer.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 2: simpleqa_0016

**Question**: What are the dimensions in centimeters of the painting "Moving House" by Vasnetsov?

**Target Answer**: 53.5 x 67.2 cm

**CustomGPT Answer**: The dimensions of the painting "Moving House" by Viktor Vasnetsov are 53 cm in height and 67 cm in width.

**Metrics**:
- Domain: arts
- Complexity: 0.999
- Confidence: 0.9
- Penalty Points: 4.0

**Judge Reasoning**: The gold target is 53.5 x 67.2 cm. The predicted answer gives 53 x 67 cm. Both dimensions are slightly off (by 0.5 cm and 0.2 cm). Since the question asks for specific dimensions and the provided values do not match the gold target, this contradicts the exact measurements.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: B

ℹ️ **Note**: All providers struggled with this question

---

### Failure 3: simpleqa_0022

**Question**: What is the last name of the player who got a yellow card in the 71st minute of the match between Germany and Sweden during the 2018 FIFA World Cup?

**Target Answer**: Boateng

**CustomGPT Answer**: The last name of the player who got a yellow card in the 71st minute of the match between Germany and Sweden during the 2018 FIFA World Cup is Ekdal.

**Metrics**:
- Domain: sports
- Complexity: 1.560
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target indicates the last name is Boateng. The predicted answer states it is Ekdal, which contradicts the gold target. Therefore, the answer is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: A

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 4: simpleqa_0045

**Question**: What was the song for the lip sync in Episode 5, Season 1 of RPDR?

**Target Answer**: "Stronger" by Britney Spears

**CustomGPT Answer**: The song for the lip sync in Episode 5, Season 1 of RuPaul's Drag Race was "Would I Lie To You?" by The Eurythmics.

**Metrics**:
- Domain: sports
- Complexity: 1.040
- Confidence: 1.0
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states the lip sync song was "Stronger" by Britney Spears. The predicted answer states it was "Would I Lie To You?" by Eurythmics, which directly contradicts the gold. Therefore, it is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 5: simpleqa_0066

**Question**: What was the complete name of the college in Delhi in which Ashraf Abbasi, the first Deputy Speaker of the National Assembly of Pakistan, studied?

**Target Answer**: Lady Hardinge Medical College

**CustomGPT Answer**: The complete name of the college in Delhi where Ashraf Abbasi studied is Lady Hardinge Medical College for Girls.

**Metrics**:
- Domain: geography
- Complexity: 1.208
- Confidence: 0.64
- Penalty Points: 4.0

**Judge Reasoning**: Gold target: Lady Hardinge Medical College. Predicted: Lady Hardinge Medical College for Girls. The addition of “for Girls” changes the official name and is not in the gold. Since the instruction says contradictions or wrong info are incorrect, and the complete name asked should match the official name, the predicted includes an extra phrase not in gold. Therefore it does not match exactly and could be considered incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: A

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 6: simpleqa_0074

**Question**: In which round was Martina Trevisan eliminated from the 2020 French Open – Women's Singles?

**Target Answer**: Quarterfinals

**CustomGPT Answer**: Martina Trevisan was eliminated in the semifinals of the 2020 French Open – Women's Singles.

**Metrics**:
- Domain: arts
- Complexity: 1.130
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target says Trevisan was eliminated in the Quarterfinals, while the predicted answer claims she was eliminated in the semifinals. This directly contradicts the gold target.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 7: simpleqa_0143

**Question**: What is the name of the organization to which the Society of Illustrators sold the rights to their Illustrator Show skits in 1925?

**Target Answer**: Shubert Organization

**CustomGPT Answer**: The Society of Illustrators sold the rights to their Illustrator Show skits in 1925 to the Shubert family, who used them for their Broadway productions of "Artists and Models."

**Metrics**:
- Domain: entertainment
- Complexity: 1.365
- Confidence: 0.8
- Penalty Points: 4.0

**Judge Reasoning**: The gold target specifies the organization as the Shubert Organization. The predicted answer states “the Shubert family,” which is not the same as naming the organization. While related, it does not match the specified organizational name and thus contradicts the exact required entity.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 8: simpleqa_0147

**Question**: What day, month, and year did New Zealand's Prime Minister, Christopher Luxon, marry his wife Amanda?

**Target Answer**: 8 January 1994

**CustomGPT Answer**: Christopher Luxon married his wife Amanda in January 1994.

**Metrics**:
- Domain: history
- Complexity: 1.450
- Confidence: 0.9
- Penalty Points: 4.0

**Judge Reasoning**: The gold target specifies a specific date: 8 January 1994. The predicted answer states only “January 1994” without the exact day. While it does not contradict the gold target, it is incomplete since the question asks for day, month, and year. According to rules, to be correct it must contain key information; missing the day means it lacks key detail.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 9: simpleqa_0154

**Question**: Where was the first B.A.S.S. Bassmaster Tournament held?

**Target Answer**: Lake Mead

**CustomGPT Answer**: The first B.A.S.S. Bassmaster Tournament, known as the All-American Bass Tournament, was held on Beaver Lake, Arkansas.

**Metrics**:
- Domain: general
- Complexity: 0.810
- Confidence: 0.98
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states the first B.A.S.S. Bassmaster Tournament was held at Lake Mead. The predicted answer claims it was held on Beaver Lake, Arkansas. This directly contradicts the gold target.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 10: simpleqa_0204

**Question**: What was the first season in which the number of houseguests for the American version of "Big Brother" increased?

**Target Answer**: 2

**CustomGPT Answer**: The first season in which the number of HouseGuests for the American version of "Big Brother" increased was Big Brother 5, which featured a total of 14 HouseGuests, an increase from previous editions.

**Metrics**:
- Domain: mathematics
- Complexity: 1.347
- Confidence: 0.93
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states the correct season is 2. The predicted answer claims it was Big Brother 5. This directly contradicts the gold target, so it is incorrect.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: B

ℹ️ **Note**: All providers struggled with this question

---

### Failure 11: simpleqa_0211

**Question**: In which year were the two novel RNA viruses, distantly related to pestiviruses and coltiviruses, detected in the genomes of dead Manis javanica and Manis pentadactyla?

**Target Answer**: 2020

**CustomGPT Answer**: The two novel RNA viruses, distantly related to pestiviruses and coltiviruses, were detected in the genomes of dead Manis javanica and Manis pentadactyla in the year 2018.

**Metrics**:
- Domain: history
- Complexity: 1.335
- Confidence: 0.99
- Penalty Points: 4.0

**Judge Reasoning**: The gold target year is 2020. The predicted answer states 2018, which contradicts the gold target. Therefore, it is incorrect.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: A

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 12: simpleqa_0226

**Question**: Which lake in Kashmir is connected to the Khushal Sar and Gil Sar lakes via a channel known as Nallah Amir Khan?

**Target Answer**: Nigeen Lake

**CustomGPT Answer**: According to my knowledge base, Anchar Lake in Kashmir is connected to the Khushal Sar and Gil Sar lakes via a channel known as "Amir Khan Nallah."

**Metrics**:
- Domain: general
- Complexity: 1.423
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states Nigeen Lake is connected to Khushal Sar and Gil Sar via Nallah Amir Khan. The predicted answer claims Anchar Lake is connected via that channel. This contradicts the gold target. Therefore, it is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 13: simpleqa_0293

**Question**: Who was named Pharmacist of the Year in 1978 by the California Pharmacists Association?

**Target Answer**: Mary Munson Runge

**CustomGPT Answer**: According to my knowledge base, Michael Pastrick was named Pharmacist of the Year in 1978 by the California Pharmacists Association.

**Metrics**:
- Domain: history
- Complexity: 1.299
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states Mary Munson Runge was named Pharmacist of the Year in 1978 by the California Pharmacists Association. The predicted answer claims Michael Pastrick received it in 1978, which directly contradicts the gold target. Therefore, it is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 14: simpleqa_0310

**Question**: How old was Montreal native Charles Whitlaw in 1846 when he bought a grist mill on Grand River Street from Robert Kirkwood in Paris, Ontario?

**Target Answer**: Twenty two

**CustomGPT Answer**: Charles Whitlaw was born in 1823. He bought a grist mill in Paris in 1846. Therefore, in 1846, Charles Whitlaw was 23 years old.

**Metrics**:
- Domain: geography
- Complexity: 1.632
- Confidence: 0.98
- Penalty Points: 4.0

**Judge Reasoning**: The gold target says he was twenty two in 1846. The predicted answer states he was 23 years old. This contradicts the gold target, so it is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 15: simpleqa_0325

**Question**: How many years was Tomb Raider: The Ride at Kings Island in operation before being rethemed?

**Target Answer**: 5

**CustomGPT Answer**: Tomb Raider: The Ride at Kings Island opened to the public on April 5, 2002, and was rethemed after the 2007 season. This means it operated under the Tomb Raider theme for approximately 6 years before being rethemed.

**Metrics**:
- Domain: history
- Complexity: 1.751
- Confidence: 0.96
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states the ride was in operation for 5 years before being rethemed. The predicted answer claims approximately 6 years (2002 to after 2007 season). This contradicts the gold target’s 5 years.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: B

ℹ️ **Note**: All providers struggled with this question

---

### Failure 16: simpleqa_0324

**Question**: Who was the Guy Medal in Gold awarded to in 1973?

**Target Answer**: David Cox

**CustomGPT Answer**: The Guy Medal in Gold was awarded to Robin Plackett in 1973.

**Metrics**:
- Domain: history
- Complexity: 0.699
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states the 1973 Guy Medal in Gold was awarded to David Cox. The predicted answer claims it was awarded to Robin Plackett, which contradicts the gold target. Therefore, it is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: A

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 17: simpleqa_0344

**Question**: On what day, month, and year (in A.D.) was the Rastriya Prajatantra Party, a constitutional monarchist and Hindu nationalist political party in Nepal, founded?

**Target Answer**: 29 May 1990

**CustomGPT Answer**: The Rastriya Prajatantra Party was founded in 1990 A.D. My knowledge base does not provide the exact day and month of its founding.

**Metrics**:
- Domain: history
- Complexity: 1.375
- Confidence: 0.9
- Penalty Points: 4.0

**Judge Reasoning**: The gold target specifies the exact day, month, and year: 29 May 1990. The predicted answer only provides the year (1990 A.D.) and explicitly states it does not have the exact day and month. Since the question asks for the day, month, and year, the predicted answer is incomplete and thus does not contain all key information from the gold target.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 18: simpleqa_0377

**Question**: In what position did Romania finish in the 2022 Rugby Europe Championship?

**Target Answer**: Second position

**CustomGPT Answer**: Romania finished in third place in the 2022 Rugby Europe Championship.

**Metrics**:
- Domain: sports
- Complexity: 0.940
- Confidence: 0.98
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states Romania finished in second position. The predicted answer claims Romania finished in third place. This directly contradicts the gold target, so it is incorrect.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: A

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 19: simpleqa_0378

**Question**: Before The New 52, who was responsible for the death of Ratcatcher?

**Target Answer**: OMAC

**CustomGPT Answer**: Before The New 52, Ratcatcher (Otis Flannegan) was killed by a civilian during the events of Infinite Crisis.

**Metrics**:
- Domain: general
- Complexity: 1.270
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states OMAC was responsible. The predicted answer says he was killed by a civilian during Infinite Crisis, which contradicts the gold. Therefore it is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 20: simpleqa_0398

**Question**: On what day, month, and year did the Canadian Centre for Inquiry's Think Again! TV document one of Popoff's performances in Toronto?

**Target Answer**: May 26, 2011

**CustomGPT Answer**: The Canadian Centre for Inquiry's Think Again! TV documented one of Peter Popoff's performances in Toronto in May 2011. My knowledge base does not provide the specific day within that month.

**Metrics**:
- Domain: history
- Complexity: 1.395
- Confidence: 0.88
- Penalty Points: 4.0

**Judge Reasoning**: The gold target specifies the exact date: May 26, 2011. The predicted answer only gives “May 2011” and explicitly states it does not provide the specific day. Since the question asks for day, month, and year, the predicted answer is incomplete and does not match the required specificity, despite being consistent on month and year. According to rules, lacking key information (the day) makes it incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 21: simpleqa_0399

**Question**: Who was the referee in the rugby match between Georgia and Portugal that was part of the 2022 Rugby Europe Championship on February 6, 2022?

**Target Answer**: Romain Poite

**CustomGPT Answer**: The referee for the rugby match between Georgia and Portugal in the 2022 Rugby Europe Championship on February 6, 2022, was Manuel Bottino from Italy.

**Metrics**:
- Domain: arts
- Complexity: 1.384
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states the referee was Romain Poite. The predicted answer claims it was Manuel Bottino from Italy, which contradicts the gold target. Therefore, it is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 22: simpleqa_0428

**Question**: In 2001, in which exhibition did Julie Mehretu participate at the Walker Art Center?

**Target Answer**: Painting at the Edge of the World

**CustomGPT Answer**: In 2001, Julie Mehretu participated in the exhibition "Unleashed" at the Walker Art Center in Minneapolis.

**Metrics**:
- Domain: arts
- Complexity: 1.047
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target exhibition is "Painting at the Edge of the World." The predicted answer states "Unleashed" at the Walker Art Center, which contradicts the gold target. Therefore, it is incorrect.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: B

ℹ️ **Note**: All providers struggled with this question

---

### Failure 23: simpleqa_0466

**Question**: Who was the 7th Chief Minister of Tamil Nadu?

**Target Answer**: Edappadi Karuppa Palaniswami.

**CustomGPT Answer**: The 7th Chief Minister of Tamil Nadu was M. G. Ramachandran.

**Metrics**:
- Domain: general
- Complexity: 0.717
- Confidence: 0.93
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states the 7th Chief Minister of Tamil Nadu is Edappadi Karuppa Palaniswami. The predicted answer claims it was M. G. Ramachandran. This directly contradicts the gold target, so it is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 24: simpleqa_0474

**Question**: In what year was the talking head of Madame Leota updated to float around the Séance Room at Disneyland?

**Target Answer**: 2004

**CustomGPT Answer**: The talking head of Madame Leota was updated to float around the Séance Room at Disneyland in 2005.

**Metrics**:
- Domain: history
- Complexity: 1.379
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target year is 2004, while the predicted answer states 2005. This directly contradicts the gold target, so it is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 25: simpleqa_0481

**Question**: What patch for the original Dark Souls made it so the Cracked Red Eye Orb is no longer consumed when connecting to an invasion fails?

**Target Answer**: 1.04

**CustomGPT Answer**: The patch that made it so the Cracked Red Eye Orb is no longer consumed when connecting to an invasion fails was patch 1.05 for the original Dark Souls.

**Metrics**:
- Domain: mathematics
- Complexity: 1.584
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states patch 1.04. The predicted answer states patch 1.05. This directly contradicts the gold target, so it is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 26: simpleqa_0521

**Question**: What were the day, month, and year of the Aseprite v1.3-beta1 release?

**Target Answer**: May 26th, 2021

**CustomGPT Answer**: Aseprite v1.3-beta1 was released in May 2021.

**Metrics**:
- Domain: history
- Complexity: 1.050
- Confidence: 0.9
- Penalty Points: 4.0

**Judge Reasoning**: The gold target specifies an exact date: May 26th, 2021. The predicted answer only states May 2021 without the specific day. While it doesn't contradict the month and year, it lacks the day required by the question. Since the grading rules require key information from the gold target and the question explicitly asks for day, month, and year, the predicted answer is incomplete and thus incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 27: simpleqa_0532

**Question**: What song's music video did Metal Injection rank at number 9 on the list of Top 15 Metal Viral Videos of the Year on December 8, 2011?

**Target Answer**: ド・キ・ド・キ☆モーニング[ Doki Doki☆Morning ] by BABYMETAL

**CustomGPT Answer**: The music video ranked at number 9 on Metal Injection's list of Top 15 Metal Viral Videos of the Year on December 8, 2011, is "JapPop Metal Band with Young Girls on Vocals."

**Metrics**:
- Domain: history
- Complexity: 1.200
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target specifies the song is “Doki Doki☆Morning” by BABYMETAL. The predicted answer refers vaguely to “JapPop Metal Band with Young Girls on Vocals,” which does not explicitly identify the song or artist and does not match the gold target. Therefore it is incorrect.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: B

ℹ️ **Note**: All providers struggled with this question

---

### Failure 28: simpleqa_0542

**Question**: Who did Maulana Azad describe as the "Muslim Lord Haw-Haw" in India?

**Target Answer**: Muhammad Ali Jinnah

**CustomGPT Answer**: According to my knowledge base, it was Muhammad Ali Jinnah who described Maulana Azad as the "Muslim Lord Haw-Haw" and a "Congress Showboy," not the other way around. Jinnah used these phrases to criticize Azad for being too close to the Congress and for allegedly allowing Muslims to be culturally and politically dominated by the Hindu community. "Lord Haw-Haw" was a nickname for William Joyce, an American broadcaster who broadcasted Nazi propaganda to Britain from Germany in 1940. The phrases used by Jinnah against Azad became associated with Azad's name as President of the Indian National Congress.

**Metrics**:
- Domain: general
- Complexity: 1.330
- Confidence: 0.96
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states that Maulana Azad described Muhammad Ali Jinnah as the 'Muslim Lord Haw-Haw'. The predicted answer claims the opposite: that Jinnah described Azad as the 'Muslim Lord Haw-Haw'. This directly contradicts the gold target, so it is incorrect.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: B

ℹ️ **Note**: All providers struggled with this question

---

### Failure 29: simpleqa_0553

**Question**: What were the month, day, and year when the construction of the UN headquarters in New York City was completed?

**Target Answer**: October 9, 1952

**CustomGPT Answer**: The construction of the United Nations headquarters in New York City was completed on October 10, 1952.

**Metrics**:
- Domain: history
- Complexity: 1.560
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target date is October 9, 1952. The predicted answer states October 10, 1952, which contradicts the gold target by one day. Therefore it is incorrect per the grading rules.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: A

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 30: simpleqa_0549

**Question**: What did Daemon say to Vaemond before killing him in HOTD Season 1?

**Target Answer**: "Say it."

**CustomGPT Answer**: Before killing Vaemond in House of the Dragon Season 1, Daemon quipped, "he can keep his tongue," after beheading Vaemond, who had just called Rhaenyra's children bastards and her a whore. This occurred after King Viserys declared he would have Vaemond's tongue for his outburst, but Daemon acted first by killing him.

**Metrics**:
- Domain: sports
- Complexity: 1.285
- Confidence: 0.96
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states Daemon said "Say it." before killing Vaemond. The predicted answer instead claims Daemon said "he can keep his tongue" after the beheading. This contradicts the required quote and timing (before vs after). Therefore it's incorrect per rules.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: B

ℹ️ **Note**: All providers struggled with this question

---

### Failure 31: simpleqa_0556

**Question**: As of which month and year did StatCounter estimate that Chrome has a 65% worldwide browser market share (after peaking at 72.38% in November 2018) on personal computers?

**Target Answer**: April 2024

**CustomGPT Answer**: StatCounter estimated that Chrome had a 65% worldwide browser market share on personal computers after peaking at 72.38% in November 2018. However, the specific month and year for the 65% estimate is not directly provided in my knowledge base.

**Metrics**:
- Domain: history
- Complexity: 1.732
- Confidence: 0.96
- Penalty Points: 4.0

**Judge Reasoning**: The question asks for a specific month and year: April 2024. The predicted answer does not provide a month and year; it states that the specific month and year are not provided. Therefore, it fails to include the key information from the gold target and is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 32: simpleqa_0580

**Question**: What is the name of the exhibition that Zanele Muholi introduced in 2009?

**Target Answer**:  Innovative Women

**CustomGPT Answer**: In 2009, Zanele Muholi founded Inkanyiso, a forum for queer and visual activist media. However, if you are asking specifically about an exhibition introduced in 2009, my knowledge base does not provide the name of a specific exhibition by Zanele Muholi from that year. Please reach out to support for further help.

**Metrics**:
- Domain: general
- Complexity: 0.899
- Confidence: 0.98
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states the exhibition name is "Innovative Women." The predicted answer does not provide this name and instead discusses Inkanyiso and uncertainty. It fails to provide the correct exhibition name and thus does not match the gold target.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 33: simpleqa_0626

**Question**: Who was the 6th Prime Minister of Nepal?

**Target Answer**: Fateh Jang Shah

**CustomGPT Answer**: The 6th Prime Minister of Nepal was Fatte Jang Chautaria.

**Metrics**:
- Domain: general
- Complexity: 0.650
- Confidence: 0.9
- Penalty Points: 4.0

**Judge Reasoning**: The gold target is Fateh Jang Shah. The predicted answer states Fatte Jang Chautaria. Although the first and middle names are phonetically similar (Fateh/Fatte), the surname/title differs: Shah vs. Chautaria. This is a substantive mismatch; thus it contradicts the gold target.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: B

ℹ️ **Note**: All providers struggled with this question

---

### Failure 34: simpleqa_0648

**Question**: What Serbian player played in the quarterfinals of the 2018 Madrid Open men's singles?

**Target Answer**: Dušan Lajović

**CustomGPT Answer**: The Serbian player who played in the quarterfinals of the 2018 Madrid Open men's singles was Novak Djokovic.

**Metrics**:
- Domain: arts
- Complexity: 1.046
- Confidence: 0.98
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states the Serbian player was Dušan Lajović. The predicted answer says Novak Djokovic. This directly contradicts the gold target. Therefore, the answer is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 35: simpleqa_0704

**Question**: As of 2022, in which years did the Pakistani team not participate in the FIH World Cup?

**Target Answer**: 2014

**CustomGPT Answer**: As of 2022, the Pakistani men's national field hockey team did not participate in the FIH World Cup in the following years:

- 2014 (The Hague edition)
- 2023 (Bhubaneswar and Rourkela edition)

These are the only two editions up to 2022 where Pakistan failed to qualify and did not take part in the tournament.

**Metrics**:
- Domain: history
- Complexity: 1.241
- Confidence: 0.9
- Penalty Points: 4.0

**Judge Reasoning**: The gold target lists only 2014 as the year Pakistan did not participate as of 2022. The predicted answer includes 2014 and also adds 2023. Including 2023 contradicts the gold target constraint (as of 2022) and adds an extra non-participation year, making it inconsistent with the gold target. Therefore it's incorrect under the grading rules.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: B

ℹ️ **Note**: All providers struggled with this question

---

### Failure 36: simpleqa_0717

**Question**: How many DLCs were released for Elder Scrolls V: Skyrim as of December 5, 2012?

**Target Answer**: 3

**CustomGPT Answer**: As of December 5, 2012, there were two DLCs released for The Elder Scrolls V: Skyrim: Dawnguard and Hearthfire. The third DLC, Dragonborn, was released on December 4, 2012, but only for Xbox 360; it was not yet available on other platforms at that time.

**Metrics**:
- Domain: general
- Complexity: 1.410
- Confidence: 0.94
- Penalty Points: 4.0

**Judge Reasoning**: Gold target says 3 DLCs as of Dec 5, 2012. Predicted answer claims only two, arguing Dragonborn released Dec 4 but only on Xbox 360 and implies not counted. This contradicts the gold target; platform exclusivity doesn’t change the count. Therefore incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: A

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 37: simpleqa_0768

**Question**: What title did the Royal Academy of Arts appoint to Cornelia Parker in 2010?

**Target Answer**: Officer of the Order of the British Empire (OBE)

**CustomGPT Answer**: In 2010, the Royal Academy of Arts elected Cornelia Parker as a Royal Academician.

**Metrics**:
- Domain: arts
- Complexity: 1.189
- Confidence: 0.98
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states Cornelia Parker was appointed Officer of the Order of the British Empire (OBE) in 2010. The predicted answer claims she was elected a Royal Academician by the Royal Academy of Arts in 2010. These are different honors from different institutions; the predicted answer contradicts the gold target and does not contain the key information.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: A

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 38: simpleqa_0765

**Question**: Which award and in which category did the animated series "Avatar: The Last Airbender" win in 2006?

**Target Answer**: Annie Awards, Storyboarding in an Animated Television Production

**CustomGPT Answer**: In 2006, "Avatar: The Last Airbender" won the Annie Award for Character Animation in a Television Production for Yu Jae Myung's animation in the episode "The Blind Bandit" and also won the Annie Award for Directing in an Animated Television Production for Giancarlo Volpe for the episode "The Drill".

**Metrics**:
- Domain: history
- Complexity: 1.361
- Confidence: 0.96
- Penalty Points: 4.0

**Judge Reasoning**: Gold target says the award was the Annie Awards, category: Storyboarding in an Animated Television Production. The predicted answer claims Character Animation in a Television Production and Directing in an Animated Television Production, which contradicts the specified category. Thus it does not match the gold target.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 39: simpleqa_0814

**Question**: In what year, month, and place was Rahat Kazmi, the Pakistani actor, born?

**Target Answer**: June 1946, Shimla, Punjab, British India

**CustomGPT Answer**: Rahat Kazmi was born in Shimla, Punjab, British India, on 30 June 1944.

**Metrics**:
- Domain: history
- Complexity: 1.109
- Confidence: 0.97
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states June 1946, Shimla, Punjab, British India. The predicted answer gives Shimla, Punjab, British India (place matches) but says 30 June 1944, which contradicts the year (1946 vs 1944). Because of the incorrect year, it contradicts the gold target and is incorrect.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: A

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 40: simpleqa_0827

**Question**: What is the resolution of the Cat B15 Q in pixels?

**Target Answer**: 480 x 800

**CustomGPT Answer**: The resolution of the Cat B15Q is 800x480 pixels.

**Metrics**:
- Domain: general
- Complexity: 0.682
- Confidence: 0.9
- Penalty Points: 4.0

**Judge Reasoning**: The gold target resolution is 480 x 800. The predicted answer states 800x480, which reverses the dimensions and contradicts the specified order. This is considered incorrect per the rules.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: A

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 41: simpleqa_0832

**Question**: Who was the first Deputy Chief Minister of Jammu and Kashmir?

**Target Answer**: Mirza Afzal Beg

**CustomGPT Answer**: The first Deputy Chief Minister of Jammu and Kashmir was Bakshi Ghulam Mohammad.

**Metrics**:
- Domain: general
- Complexity: 1.074
- Confidence: 0.99
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states the first Deputy Chief Minister of Jammu and Kashmir was Mirza Afzal Beg. The predicted answer names Bakshi Ghulam Mohammad, which contradicts the gold target. Therefore, it is incorrect.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: B

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 42: simpleqa_0947

**Question**: How many A-frame structures does the 1961 Stebel House in Los Angeles comprise?

**Target Answer**: 3

**CustomGPT Answer**: The 1961 Stebel House in Los Angeles comprises a dramatic A-frame rafter design supported by a beamed and bolted X-frame foundation. The structure is noted for its singular, striking A-frame form, which is a defining architectural feature of the house. There is no indication in my knowledge base of multiple separate A-frame structures; the house is characterized by its primary, cohesive A-frame design.

**Metrics**:
- Domain: general
- Complexity: 1.228
- Confidence: 0.98
- Penalty Points: 4.0

**Judge Reasoning**: The gold target states the Stebel House comprises 3 A-frame structures. The predicted answer claims it has a singular A-frame and denies multiple structures. This contradicts the gold target.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: A

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---

### Failure 43: simpleqa_0945

**Question**: What was the full three-word name of the crystal that the gnome who piloted the airship in the motion simulator Questor, which first opened at Busch Gardens Williamsburg in 1990, was seeking as the ultimate goal of his expedition?

**Target Answer**: Crystal of Zed

**CustomGPT Answer**: The full three-word name of the crystal sought by the gnome Alwyn in the Questor motion simulator at Busch Gardens Williamsburg was the "Crystal of Zedd."

**Metrics**:
- Domain: general
- Complexity: 1.338
- Confidence: 0.9
- Penalty Points: 4.0

**Judge Reasoning**: Gold target is “Crystal of Zed.” Predicted answer says “Crystal of Zedd.” The extra ‘d’ changes the specific name; semantic meaning depends on exact proper noun. This contradicts the gold target’s spelling and is not the same entity. Therefore incorrect.

**Competitive Performance**:
- OpenAI RAG: B
- OpenAI Vanilla: B

ℹ️ **Note**: All providers struggled with this question

---

### Failure 44: simpleqa_0974

**Question**: What day, month, and year did the actor Dylan Sprouse marry Barbara Palvin?

**Target Answer**: 15 of July of 2023

**CustomGPT Answer**: Dylan Sprouse married Barbara Palvin in July 2023. The ceremony took place in the bride's home country of Hungary, outside of Budapest. The exact day is not specified in my knowledge base.

**Metrics**:
- Domain: history
- Complexity: 1.165
- Confidence: 0.9
- Penalty Points: 4.0

**Judge Reasoning**: The gold target specifies the exact date: 15 July 2023. The predicted answer only gives July 2023 and explicitly states the exact day is not specified. It lacks the day component required by the question and gold target. While it doesn't contradict the month/year, it is incomplete and thus not meeting the key information requirement.

**Competitive Performance**:
- OpenAI RAG: A
- OpenAI Vanilla: A

⚠️ **Critical**: Competitors succeeded where CustomGPT failed

---


## Engineering Recommendations

### Priority 1: Immediate Actions

1. **Confidence Calibration Crisis**: 29 failures had >95% confidence
   - Review confidence scoring algorithm
   - Implement uncertainty estimation improvements
   - Add confidence validation against retrieval quality

2. **Competitive Gap**: Competitors succeeded on 34/44 failed questions
   - Analyze competitor knowledge sources
   - Review retrieval algorithm effectiveness
   - Benchmark against OpenAI RAG capabilities

3. **Domain Focus**: 17 failures in history domain
   - Expand history knowledge base coverage
   - Review history-specific retrieval patterns
   - Validate history fact accuracy

### Priority 2: System Improvements

1. **Quality Score Impact**: Current penalty ratio of 4.0 is severe
   - Each wrong answer costs 4.0 quality points
   - Consider implementing graduated penalties
   - Evaluate abstention vs incorrect answer trade-offs

2. **Knowledge Base Enhancement**:
   - Add fact verification layer
   - Implement source confidence scoring
   - Review document indexing quality

3. **Retrieval Algorithm**:
   - Analyze retrieval relevance for failed questions
   - Implement multi-hop reasoning capabilities
   - Add semantic similarity improvements

### Priority 3: Long-term Strategy

1. **Continuous Monitoring**:
   - Implement real-time confidence calibration tracking
   - Set up automated competitive benchmarking
   - Create domain-specific performance dashboards

2. **Model Training**:
   - Fine-tune on identified failure patterns
   - Implement active learning from failures
   - Add uncertainty quantification training



---
*This report was automatically generated from evaluation run run_20250929_015010_984*
*Report generated at: 2025-09-29T02:47:49.921396*
