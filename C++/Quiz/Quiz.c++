#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

void Questions() {
    int points = 0;
    vector<string> Ans1 = {"Neil A.","Alden Armstrong","Neil Armstrong","Neil Alden Armstrong"};
    vector<string> Ans2 = {"sun","Sun","SUN"};
    vector<string> Ans3 = {"Everest","Mt.Everest","Mount Everest"};
    vector<string> Ans4 = {"moon","MOON","Moon"};
    vector<string> Ans5 = {"Pluto","pluto","PLUTO"};
    vector<string> Ans6 ={"Homosapiens","HOMOSAPIENS","Homo Sapiens","Homo sapiens","Homo-sapiens","Homo-Sapiens","Homosapien","HOMOSAPIEN","Homo Sapien","Homo sapien","Homo-sapien","Homo-Sapien"};
    vector<string> Ans7 ={"Gravity","gravity","GRAVITY"};
    vector<string> Ans8 ={"mammals","MAMMALS","mammal","MAMMAL"};
    vector<string> Ans9 ={"Aryabhata","Aryabhatt","ARYABHATA","ARYABHATT","aryabhatt","aryabhata"};
    vector<string> Ans10={"east","East","EAST"};
    string Answer;
    while (true) {
        cout << "Who was the first man to step on moon ? \n";
        getline(cin, Answer);
        if (find(Ans1.begin(), Ans1.end(), Answer) != Ans1.end()) {
            cout << "CORRECT ANSWER!!!!\n";
            points +=1;
        } else {
            cout << "INCORRECT ANSWER!!!!\n";
        }
        
        cout << "Name the largest star in our solar system  \n";
        getline(cin, Answer);
        if (find(Ans2.begin(), Ans2.end(), Answer) != Ans2.end()) {
            cout << "CORRECT ANSWER!!!!\n";
            points +=1;
        } else {
            cout << "INCORRECT ANSWER!!!!\n";
        }
        
        cout << "What's The Highest Mountain Cliff ? \n";
        getline(cin, Answer);
        if (find(Ans3.begin(), Ans3.end(), Answer) != Ans3.end()) {
            cout << "CORRECT ANSWER!!!!\n";
            points +=1;
        } else {
            cout << "INCORRECT ANSWER!!!!\n";
        }
        
        cout << "What is the name of earth's the natural satellite ? \n";
        getline(cin, Answer);
        if (find(Ans4.begin(), Ans4.end(), Answer) != Ans4.end()) {
            cout << "CORRECT ANSWER!!!!\n";
            points +=1;
        } else {
            cout << "INCORRECT ANSWER!!!!\n";
        }
        
        cout << "Name The Dwarf Planet In Our Solar System  \n";
        getline(cin, Answer);
        if (find(Ans5.begin(), Ans5.end(), Answer) != Ans5.end()) {
            cout << "CORRECT ANSWER!!!!\n";
            points += 1;
        } else {
            cout << "INCORRECT ANSWER!!!!\n";
        }
        
        cout << "What is the scientific name of humans ? \n";
        getline(cin, Answer);
        if (find(Ans6.begin(), Ans6.end(), Answer) != Ans6.end()) {
            cout << "CORRECT ANSWER!!!!\n";
            points +=1;
        } else {
            cout << "INCORRECT ANSWER!!!!\n";
        }
        
        cout << "Name the force which pulls us to the ground \n";
        getline(cin, Answer);
        if (find(Ans7.begin(), Ans7.end(), Answer) != Ans7.end()) {
            cout << "CORRECT ANSWER!!!!\n";
            points +=1;
        } else {
            cout << "INCORRECT ANSWER!!!!\n";
        }
        
        cout << "Name the type of animal that milkfeed their babies \n";
        getline(cin, Answer);
        if (find(Ans8.begin(), Ans8.end(), Answer) != Ans8.end()) {
            cout << "CORRECT ANSWER!!!!\n";
            points +=1;
        } else {
            cout << "INCORRECT ANSWER!!!!\n";
        }
        
        cout << "Who discovered zero ? \n";
        getline(cin, Answer);
        if (find(Ans9.begin(), Ans9.end(), Answer) != Ans9.end()) {
             cout << "CORRECT ANSWER!!!!\n";
             points += 1;
        } else {
            cout << "INCORRECT ANSWER!!!!\n";
        }
        
        cout << "From which direction does sun rise from ? \n";
        getline(cin, Answer);
        if (find(Ans10.begin(), Ans10.end(), Answer) != Ans10.end()) {
            cout << "CORRECT ANSWER!!!!\n";
            points += 1;
        } else {
            cout << "INCORRECT ANSWER!!!!\n";
        }
        
        string Name;
        if (points <= 5) {
            cout << "Congrats " << Name << " You Scored " << points << " points out of 10! Nice Try\n";
            return;
        } else if (points <= 8) {
            cout << "Congrats " << Name << " You Scored " << points << " points out of 10! Great Job!\n";
            return;
        } else if (points <= 10) {
            cout << "Congrats " << Name << " You Scored " << points << " points out of 10! Perfect!\n";
            return;
        }
    }
}

void Quiz() {
    while (true) {
        cout << "***General Knowledge Quiz*** \n1.Start Quiz \n2.Exit\n";
        string Choice;
        getline(cin, Choice);
        if (Choice == "2") {
            break;
        }
        if (Choice == "1") {
            while (true) {
                cout << "***Rules*** \n1.This Quiz Has 10 questions \n2.You'll be rewarded 1 point for each correct answer \n3. There's no negative Marking \n4.Points system: \n 1-5 points Nice Try \n 6-8 Great Job! \n 9-10 Perfect!!\n";
                cout << "Do you wish to continue (yes/no):";
                getline(cin, Choice);
                if (Choice == "no") {
                    break;
                }
                if (Choice == "yes") {
                    Questions();
                    break;
                }
            }
        }
    }
}

int main() {
    Quiz();
    return 0;
}
