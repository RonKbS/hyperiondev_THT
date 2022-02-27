

## SECTION C
### OPTION 1
 To complete this assignment, [num-words](https://github.com/salmanm/num-words) library is [forked](https://github.com/RonKbS/num-words), reviewed and refactored to answer option 1 of section C.
- Review
    - The library makes great use of regex-es to enable the conversion from figures to words of numbers.
    - It has elements of the Indian numbering system which points to the creator's lack of a need for internationalization such as in [this](https://pypi.org/project/num2words/). Ajustments are therefore made to use the English system of wording numbers [here](https://github.com/RonKbS/num-words/commit/1caf280afe2df40c0134a2fb651ed159f6b5d095).
    - num-words also has a limit to the number of digits it can convert into the needed word system. Adjustments for that are therefore made [here](https://github.com/RonKbS/num-words/commit/c8262b55253b560272e45ee84787a0b437d517bb).
    - Following successful refactoring, the repository can be pulled to run tests as show below;
    ```
    $ git clone https://github.com/RonKbS/num-words.git

    $ cd <path-to-num-words>

    $ npm install

    $ npm run test
    ```
    - To make use of the library, the block below can be followed;
    ```
    # create and move into folder
    $ npm i git+https://github.com/RonKbS/num-words.git#c8262b55253b560272e45ee84787a0b437d517bb

    # create js file, say num2Words.js
    $ touch num2Words.js

    # paste in code below

    const numWords = require('num-words')
    const amountInWords = numWords(555555555)
    console.log(amountInWords)

    # run file
    $ node num2Words.js
    ```
#
### Space complexity

The package code has a worst case space complexity of O(n) after refactoring.
This conclusion comes about from the fact that it harnesses [arrays](https://medium.datadriveninvestor.com/big-o-notation-8a0a28f00813) and strings to achieve a result.
I do suspect that even though the complexity is linear, it's actual worst case will not be more than what is utilized for the whole number less than _one thousand trillion_. This is due to the fact that the arrays and strings are restricted in the amount of data they can take in, once that number is exceeded.