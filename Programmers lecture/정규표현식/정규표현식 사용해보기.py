# 정규표현식 사용해보기

# 주소록입니다. 이후 강의에서 모두 이 search_target을 사용합니다.
search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re

regex = r'0\d{1,2}[ -]?\d{3,4}[ -]?\d{3,4}'
result = re.findall(regex, search_target)  # search_target에서 regex에 해당하는 것을 찾아라 
print("\n".join(result))



#### 정규표현식 배우기

## \d
# - 숫자를 대표하는 정규표현식
# - d : digit


## \w
# - 글자를 대표하는 정규표현식
# - "a, b, c, 가, 나, 다, 1, 2"와 같은 문자와 숫자를 포함
# - 특수문자는 포함하지 않지만, _(언더스코어)는 포함


## +
# - "하나 혹은 그 이상 연결된" 
# - \d는 한글자만 찾음 But, 연결된 숫자를 찾고싶을 때는 "+" 이용
# - \d+ 는 "하나 혹은 그 이상 연결된 숫자" 라는 의미


## *
# - "0개 이상" 
# - \d* 는 "숫자가 0개 이상" 이라는 의미
### +) 자연수 찾기
#### 1. 자연수는 첫째 자리로 0을 제외한 1-9의 숫자로 이루어짐
#### 2. 그 뒤에는 0-9까지 어떤 숫자든 가능
####  →  [1-9]\d*


## ?
# - "있거나 없거나"
### +) 전화번호 찾기
#### 1. 전화번호는 숫자 사이에 '-'를 포함하거나 포함하지 않을 수 있음
#### ex)  0283729465,  010-5632-2512 은 모두 유효한 전화번호
#### 즉, 전화번호는 연속되는 숫자 3~4개 사이에 -가 있거나 없다고 표현할 수 있음
####  →  \d+-?\d+-?\d+


##  (공백)
# - 위와 연결하여 설명
# - 전화번호는 "010 4538 6532"과 같이 공백과 함께 표현 가능
### +) 모든 전화번호 찾기
#### 1. '-'가 있거나 없다 라는 조건이 아닌
#### 2. "'-'또는 공백이 있거나 없다" 라는 조건을 써야함
####  →  [- ]?
####  최종 코드 →   \d+[- ]?\d+[- ]?\d+


## {숫자}
# - " `숫자`번 반복한다 "
# - \d{2}  는  "숫자가 연속 두번 나옴"
### +) 예제
#### - \d{2}[- ]?\d{3}[- ]?\d{4}
#### - 숫자가 연속 두번 나온 뒤 -또는 공백이 있거나 없고, 그 후 숫자가 3번 연속 나온 뒤 - 또는 공백이 있거나 없을 수 있으며, 후에 숫자가 연속하여 4번이 나옴


## {숫자1, 숫자2}
# - "숫자1부터 숫자2까지 반복한다"
# - \w{2,3}  는  "문자가 2~3번 나온다"
### +) 전화번호 찾기
#### 1. 전화번호 자릿수는 처음(2~3자리), 중간(3~4)자리, 끝(4자리)로 이루어져 있다.
####  →  \d{2,3}[- ]?\d{3,4}[- ]?\d{4}


## [ ]  -  몇 개 중에 고르기
# - 정규표현식에서 대괄호[] 안에 글자를 넣으면 해당 글자를 모두 선택할 수 있음
### +) 예제
#### - 알파벳 중에 소문자 모음(a,e,i,o,u)만 고르고 싶을 때
####   →   [aeiou]


## [◆-◇]   -   범위에서 고르기
# - "◆ 에서부터 ◇ 까지 모두 선택하라"
### +) 예제
#### - 소문자 알파벳만 고르고 싶을 때
####  →   [a-z]


## 한글 단어 찾기
# - 한글의 첫 번째 글자는 `가`이고, 마지막 글자는 `힣`이기 때문에
# - [가-힣]+ 하여 찾을 수 있음
### +) 이 방식으로는 `ㄱㄴㄷ` 또는 `ㅏㅑㅓㅕ`와 같은 낱글자는 찾을 수 없음


#### 기타 대표문자
## \s
# - 공백문자(스페이스, 탭, 뉴라인)

## \S
# 공백 문자를 제외한 문자

## \D
# - 숫자를 제외한 문자

## \W
# - 글자 대표 문자를 제외한 글자들(특수문자, 공백 등)





# ------------------------ 추가 -----------------------------
## Java 언어로 정규표현식 다루기
# - Java로 정규표현식을 다룰 때에는 Pattern 클래스와 Matcher 클래스를 이용
### * 주의할 점 *
#### - Java에서는 `\`대신 `\\`를 사용
import java.io.Console;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class MyRegex{
    public static void main(String[] args){
        String searchTarget = "Luke Skywarker 02-123-4567 luke@daum.net\n다스베이더 070-9999-9999 darth_vader@gmail.com\nprincess leia 010 2454 3457 leia@gmail.com";

        Pattern pattern = Pattern.compile("\\w");
        Matcher matcher = pattern.matcher(searchTarget);
        while(matcher.find()){
            System.out.println(matcher.group(0));
        }
    }
}


## Javascript로 정규표현식 다루기
# - Javascript로 정규표현식을 다룰 때에는 String class의 match 함수를 이용
var searchTarget = "Luke Skywarker 02-123-4567 luke@daum.net\
다스베이더 070-9999-9999 darth_vader@gmail.com\
princess leia 010 2454 3457 leia@gmail.com";

# 아래 코드의 /와 /g가운데에 정규표현식을 넣으세요.
# g는 global의 약자로, 정규표현식과 일치하는 모든 내용을 찾아오라는 옵션입니다.
#
var regex = /\d/g;
console.log(searchTarget.match(regex));


## C# 언어로 정규표현식 다루기
# - C# 으로 정규표현식을 다룰 때에는 Regex.matches라는 메소드 이용
### * 주의할 점 *
#### - C# 에서는 `\`대신 `\\`를 사용
using System;
using System.Text.RegularExpressions;

public class RegexTest {
    public static void Main() {
        string regex = "\\d";
        string searchTarget = "Luke Skywarker 02-123-4567 luke@daum.net\n다스베이더 070-9999-9999 darth_vader@gmail.com\nprincess leia 010 2454 3457 leia@gmail.com";

        foreach (Match m in Regex.Matches(searchTarget, regex)){
            Console.WriteLine(m.Value);
        }
    }
}
