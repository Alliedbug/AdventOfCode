#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const string FILENAME = "SimInput.txt";
const int MAX = 2500;


int main() {
	ifstream infile;
	int count = 0;
	string inputList[MAX];
	
  infile.open(FILENAME);
  if (infile.fail()) {
    cout << "file error... press enter..." << endl;
    cin.get();
    return 0;
  } 

	while (getline(infile, inputList[count])) {
    count++;
  }
	/* for (int i = 0; i < count; i++) {
		cout << inputList[i] << ' ' << endl;
	} */

	// A/X - Rock
  // B/Y - Paper
	// C/Z - Scissors

  //  X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

	int totalScore = 0;
	int currentScore = 0;
	for (int i = 0; i < count; i++) {
		char us =  inputList[i][2];
		char them = inputList[i][0];
    
		if (us == 'X') {
			if (them == 'A') {
        currentScore += 3;
      }
      else if (them == 'C') {
				currentScore += 2;
      }
			else {
				currentScore++;
			}
		}
		else if(us == 'Y') {
			currentScore += 3;
			if(them == 'A') {
				currentScore += 1;
			}
			else if (them == 'B') {
				currentScore += 2;
			}
			else {
				currentScore += 3;
			}
		}
		else {
			currentScore += 6;
			if(them == 'B') {
				currentScore += 3;
			}
			else if (them == 'C') {
				currentScore += 1;
			}
			else {
				currentScore += 2;
			}
		}
		totalScore += currentScore;
		currentScore = 0;
	}

	cout << totalScore << endl;
}
