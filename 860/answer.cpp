//greedy

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int fiveDollars = 0, tenDollars = 0, twentyDollars = 0;
        for (int i=0; i<bills.size(); i++){
            switch(bills[i]){
                case 5:
                    fiveDollars += 1;
                    break;
                case 10:
                    if (fiveDollars >= 1){
                        fiveDollars -= 1;
                        tenDollars += 1;
                    }else{
                        return false;
                    }
                    break;
                case 20:
                    if (  fiveDollars >= 1 && tenDollars >=1){

                        tenDollars -= 1;
                        fiveDollars -= 1;
                        twentyDollars += 1;
                    }else{
                        if (fiveDollars >= 3){
                            fiveDollars -= 3;
                            twentyDollars += 1;
                        }else{
                            return false;
                        }
                    }
                    break;
            }
        }
        return true;
    }
};
