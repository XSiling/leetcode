class Solution {
public:
    bool isValid(string s) {
        vector<char> s_stack = {};
        char currentChar;
        for(int i=0; i<s.length(); ++i){
            if (s[i] == '(' || s[i] == '{' || s[i] == '['){
                s_stack.push_back(s[i]);
            }else{
                if (s_stack.size() >= 1){
                    currentChar = s_stack.back();
                    s_stack.pop_back();
                }else{
                    return false;
                }
                
                switch(s[i]){
                    case ')':{
                        if (currentChar != '('){
                            return false;
                        }
                        break;
                    }
                    case ']':{
                        if (currentChar != '['){
                            return false;
                        }
                        break;
                    }
                    case '}':{
                        if (currentChar != '{'){
                            return false;
                        }
                        break;
                    }
                }
            }
        }
        
        if (s_stack.size() != 0){
            return false;
        }else{
            return true;
        }
    }
};
