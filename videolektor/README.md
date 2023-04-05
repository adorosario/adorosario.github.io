# CREATED USING THIS PROCESS
```
0. wget 'https://www.videolektor.cz/product-feed'
1. cat product-feed  | grep 'g:link' | perl -ne 'if (m/<g:link>(.*?)<\/g:link>/) { print "$1\n"; }' > list.txt
2. The follow steps in: https://customgpt.ai/personal-chatbot/
```
