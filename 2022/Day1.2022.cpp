#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const string FILENAME = "SimInput.txt";
const int MAX = 2263;


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

	int currentElf = 0;
	int maxElfTwo = 0;
	int maxElfThree = 0;
	int maxElf = 0;
	
	for (int i = 0; i < count; i++) {
		if (inputList[i] != "") {
			currentElf += stoi(inputList[i]);
		}
		else {
			if (maxElf < currentElf) {
				maxElfThree = maxElfTwo;
				maxElfTwo = maxElf;
				maxElf = currentElf;
			}
			else if (maxElfTwo < currentElf) {
				maxElfThree = maxElfTwo;
				maxElfTwo = currentElf;
			}
			else if (maxElfThree < currentElf) {
				maxElfThree = currentElf;
			}
			currentElf = 0;
		}
	}
	int total = maxElf + maxElfThree + maxElfTwo;
	cout << total << endl;
	
}