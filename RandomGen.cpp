#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <sys/time.h>
#include <fstream>
#ifdef __cplusplus__
  #include <cstdlib>
#else
  #include <stdlib.h>
#endif
//all them includes 
void clearscreen(){
if (system("CLS")) system("clear");
}
//windows AND linux
//make the random seed
void seedrand(){
    struct timeval time;
    gettimeofday(&time,NULL);

    // microsecond has 1 000 000
    // Assuming you did not need quite that accuracy
    // Also do not assume the system clock has that accuracy.
    srand((time.tv_sec * 1000) + (time.tv_usec / 1000));

    // The trouble here is that the seed will repeat every
    // 24 days or so.

    // If you use 100 (rather than 1000) the seed repeats every 248 days.

    // Do not make the MISTAKE of using just the tv_usec
    // This will mean your seed repeats every second.
}
std::string random_sentence(){
    //make the return var
    std::string var_to_return;
    //PRONOUNS
    std::vector<std::string> pronouns;
    pronouns.push_back("I");
    pronouns.push_back("We");
    pronouns.push_back("You");
    pronouns.push_back("They");
    int RandIndex = rand() % 4;
    var_to_return = pronouns[RandIndex] + " ";
    //VERBS
    std::vector<std::string> verbs;
    verbs.push_back("run");
    verbs.push_back("walk");
    verbs.push_back("go");
    verbs.push_back("stay here");
    verbs.push_back("eat");
    verbs.push_back("poop");
    verbs.push_back("squirt");
    verbs.push_back("applaud");
    verbs.push_back("dream");
    verbs.push_back("dance");
    RandIndex = rand() % 10;
    var_to_return = var_to_return + verbs[RandIndex] + " ";
    //PROPOSITIONS
    //pre=['with','under','over','into','onto','between','through']
    std::vector<std::string> prepositions;
    prepositions.push_back("with");
    prepositions.push_back("under");
    prepositions.push_back("over");
    prepositions.push_back("into");
    prepositions.push_back("onto");
    prepositions.push_back("between");
    prepositions.push_back("through");
    RandIndex = rand() % 7;
    var_to_return = var_to_return + prepositions[RandIndex] + " ";
    //ARTICLES
    std::vector<std::string> articles;
    articles.push_back("a");
    articles.push_back("the");
    RandIndex = rand() % 2;
    var_to_return = var_to_return + articles[RandIndex] + " ";
    //NOUNS
    std::vector<std::string> nouns;
    nouns.push_back("dog");
    nouns.push_back("cat");
    nouns.push_back("mud");
    nouns.push_back("universe");
    nouns.push_back("tree");
    nouns.push_back("forest");
    nouns.push_back("text document");
    nouns.push_back("apple");
    nouns.push_back("orange");
    nouns.push_back("leash");
    nouns.push_back("fur");
    nouns.push_back("bacon");
    nouns.push_back("adventure");
    nouns.push_back("turtle");
    nouns.push_back("nun");
    nouns.push_back("table");
    nouns.push_back("TV");
    nouns.push_back("poem");
    nouns.push_back("glockenspiel");
    nouns.push_back("dream");
    nouns.push_back("computer");
    nouns.push_back("shortstop");
    nouns.push_back("underwear");
    nouns.push_back("clown");
    nouns.push_back("pork");
    nouns.push_back("window");
    nouns.push_back("angel");
    nouns.push_back("dance");
    nouns.push_back("candy");
    nouns.push_back("song");//30th item, 29th index
    nouns.push_back("balloon");
    nouns.push_back("umbrella");
    RandIndex = rand() % 32; //number of items, NOT indexes
    var_to_return = var_to_return + nouns[RandIndex];
    var_to_return = var_to_return + ".";
    return var_to_return;
}
//main function
int main(){
    seedrand();
    std::cout<<"Do you want to (G)enerate sentences or (V)iew all sentences ever generates?";
    std::string what_to_do;
    std::cin>>what_to_do;
    while (!((what_to_do=="G") || (what_to_do=="V"))){
        std::cout<<"Do you want to (G)enerate sentences or (V)iew all sentences ever generates?";
        std::cin>>what_to_do;
    }
    if (what_to_do=="G"){
        std::ofstream file_to_write;
        std::string sentence;
        file_to_write.open("sentences.txt", std::ios::app);
        int times_to_repeat;
        std::cout<<"How many sentences do you want to generate?\n";
        std::cin>>times_to_repeat;
        clearscreen();
        for (int i=0; i<times_to_repeat; ++i) {
            sentence=random_sentence();
            std::cout<<sentence<<std::endl;
            file_to_write<<sentence<<std::endl;
        }
        file_to_write.close();
        std::cout<<"Done!"<<std::endl;
    }
    else{
        std::string line;
        std::ifstream sentences_file ("sentences.txt");
        while (getline(sentences_file,line)){
            std::cout << line << "\n";
        }
        sentences_file.close();
        std::cout<<"Done!"<<std::endl;
    }
}
