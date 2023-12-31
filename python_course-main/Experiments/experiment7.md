# 实验七 Python面向对象编程

班级： 21计科1班

学号： B20210302118

姓名： 申佳

Github地址：<https://github.com/ShenJia0722/python-from-shenjia>

CodeWars地址：<https://www.codewars.com/users/Belief_V>


---

## 实验目的

1. 学习Python类和继承的基础知识
2. 学习namedtuple和DataClass的使用

## 实验环境

1. Git
2. Python 3.10
3. VSCode
4. VSCode插件

## 实验内容和步骤

### 第一部分

Python面向对象编程

完成教材《Python编程从入门到实践》下列章节的练习：

- 第9章 类

---

### 第二部分

在[Codewars网站](https://www.codewars.com)注册账号，完成下列Kata挑战：

---

#### 第一题：面向对象的海盗

难度： 8kyu

啊哈，伙计!

你是一个小海盗团的首领。而且你有一个计划。在OOP的帮助下，你希望建立一个相当有效的系统来识别船上有大量战利品的船只。
对你来说，不幸的是，现在的人很重，那么你怎么知道一艘船上装的是黄金而不是人呢？

你首先要写一个通用的船舶类。

```python
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
```

每当你的间谍看到一艘新船进入码头，他们将根据观察结果创建一个新的船舶对象。

- `draft`吃水 - 根据船在水中的高度来估计它的重量
- `crew`船员 - 船上船员的数量

`Titanic = Ship(15, 10)`

任务

你可以访问船舶的 "draft(吃水) "和 "crew(船员)"。"draft(吃水) "是船的总重量，"船员 "是船上的人数。
每个船员都会给船的吃水增加1.5个单位。如果除去船员的重量后，吃水仍然超过20，那么这艘船就值得掠夺。任何有这么重的船一定有很多战利品!
添加方法
`is_worth_it`
来决定这艘船是否值得掠夺。

例如：

```python
Titanic.is_worth_it()
False
```

祝你好运，愿你能找到金子!

代码提交地址：
<https://www.codewars.com/kata/54fe05c4762e2e3047000add>

实验代码：
```python
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    # Your code here
    def is_worth_it(self):
        return self.draft-self.crew*1.5>20
```

---

#### 第二题： 搭建积木

难度：7kyu

写一个创建Block的类（Duh.）
构造函数应该接受一个数组作为参数，这个数组将包含3个整数，其形式为`[width, length, height]`，Block应该由这些整数创建。

定义这些方法:

- `get_width()` return the width of the `Block`
- `get_length()` return the length of the `Block`
- `get_height()` return the height of the `Block`
- `get_volume()` return the volume of the `Block`
- `get_surface_area()` return the surface area of the `Block`

例子：

```python
b = Block([2,4,6]) # create a `Block` object with a width of `2` a length of `4` and a height of `6`
b.get_width() # return 2    
b.get_length() # return 4
b.get_height() # return 6
b.get_volume() # return 48
b.get_surface_area() # return 88
```

注意： 不需要检查错误的参数。

代码提交地址：
<https://www.codewars.com/kata/55b75fcf67e558d3750000a3>

实验代码：
```python
class Block:
    # Good Luck!
    def __init__(self,args):
        self.width=args[0]
        self.length=args[1]
        self.height=args[2]
    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    def get_height(self):
        return self.height
    def get_volume(self):
        ans=self.width*self.length*self.height
        return ans
    def get_surface_area(self):
        ans1=self.width*self.length
        ans2=self.width*self.height
        ans3=self.length*self.height
        ans=2*(ans1+ans2+ans3)
        return ans
```

---

#### 第三题： 分页助手

难度：5kyu

在这个练习中，你将加强对分页的掌握。你将完成PaginationHelper类，这是一个实用类，有助于查询与数组有关的分页信息。
该类被设计成接收一个值的数组和一个整数，表示每页允许多少个项目。集合/数组中包含的值的类型并不相关。

下面是一些关于如何使用这个类的例子：

```python
helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count() # should == 2
helper.item_count() # should == 6
helper.page_item_count(0)  # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid
```

代码提交地址：
<https://www.codewars.com/kata/515bb423de843ea99400000a>

实验代码：
```python
# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        #pass
        self.collection=collection
        self.items_per_page=items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        #pass
        cnt=len(self.collection)
        return cnt
        
    # returns the number of pages
    def page_count(self):
        #pass
        cnt1=len(self.collection)
        ans=(cnt1+self.items_per_page-1)/self.items_per_page
        return int(ans)
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        #pass
        lim1=(len(self.collection))/self.items_per_page
        lim1=int(lim1)
        lim2=(len(self.collection)+self.items_per_page-1)/self.items_per_page
        lim2=int(lim2)
        ans3=(len(self.collection))%(self.items_per_page)
        if page_index>=lim2 :
              return -1
        if page_index<0 :
              return -1
        if page_index<lim1:
              return self.items_per_page
        return ans3
        
            
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
                 if item_index<0:
                       return -1
                 if item_index>=len(self.collection):
                        return -1
                 ans=(item_index)/(self.items_per_page)
                 ans=int(ans)
                 return ans
```

---

#### 第四题： 向量（Vector）类

难度： 5kyu

创建一个支持加法、减法、点积和向量长度的向量（Vector）类。

举例来说：

```python
a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
```

如果你试图对两个不同长度的向量进行加减或点缀，你必须抛出一个错误。
向量类还应该提供：

- 一个 `__str__` 方法，这样 `str(a) === '(1,2,3)'` 
- 一个equals方法，用来检查两个具有相同成分的向量是否相等。

注意：测试案例将利用用户提供的equals方法。

代码提交地址：
<https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4>

实验代码：
```python
from math import sqrt

class Vector:
    def __init__(self,args):
        self.v=tuple(x for x in args)
    
    def __str__(self):
        return str(self.v).replace(' ','')
    
    def check(self, other):
        if not len(self.v) == len(other.v):
            raise ValueError('Vectors of different length')
    
    
    def add(self,other):
        self.check(other)
        return Vector(x+y for x,y in zip(self.v,other.v))
    
    def subtract(self,other):
        self.check(other)
        return Vector(x-y for x,y in zip(self.v,other.v))
    
    def dot(self,other):
        self.check(other)
        return sum(x*y for x,y in zip(self.v,other.v))
    
    def norm(self):
        sum=0
        for x in self.v:
            sum+=x*x
        return sqrt(sum)
    def equals(self,other):
        return self.v==other.v
```

---

#### 第五题： Codewars风格的等级系统

难度： 4kyu

编写一个名为User的类，用于计算用户在类似于Codewars使用的排名系统中的进步量。

业务规则：

- 一个用户从等级-8开始，可以一直进步到8。
- 没有0（零）等级。在-1之后的下一个等级是1。
- 用户将完成活动。这些活动也有等级。
- 每当用户完成一个有等级的活动，用户的等级进度就会根据活动的等级进行更新。
- 完成活动获得的进度是相对于用户当前的等级与活动的等级而言的。
- 用户的等级进度从零开始，每当进度达到100时，用户的等级就会升级到下一个等级。
- 在上一等级时获得的任何剩余进度都将被应用于下一等级的进度（我们不会丢弃任何进度）。例外的情况是，如果没有其他等级的进展（一旦你达到8级，就没有更多的进展了）。
- 一个用户不能超过8级。
- 唯一可接受的等级值范围是-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8。任何其他的值都应该引起错误。

逻辑案例：

- 如果一个排名为-8的用户完成了一个排名为-7的活动，他们将获得10的进度。
- 如果一个排名为-8的用户完成了排名为-6的活动，他们将获得40的进展。
- 如果一个排名为-8的用户完成了排名为-5的活动，他们将获得90的进展。
- 如果一个排名-8的用户完成了排名-4的活动，他们将获得160个进度，从而使该用户升级到排名-7，并获得60个进度以获得下一个排名。
- 如果一个等级为-1的用户完成了一个等级为1的活动，他们将获得10个进度（记住，零等级会被忽略）。

代码案例：

```python
user = User()
user.rank # => -8
user.progress # => 0
user.inc_progress(-7)
user.progress # => 10
user.inc_progress(-5) # will add 90 progress
user.progress # => 0 # progress is now zero
user.rank # => -7 # rank was upgraded to -7
```

代码提交地址：
<https://www.codewars.com/kata/51fda2d95d6efda45e00004e>

实验代码：
```python
class User ():    
    def __init__ (self):
        self.RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank = -8
        self.rank_index = 0
        self.progress = 0
        
    def inc_progress (self, rank):
        rank_index = self.RANKS.index(rank)
        
        # 计算rank的差，得出可以获得多少进度
        
        # 完成的是同等级的题目
        if rank_index == self.rank_index:
            self.progress += 3
            
        # 完成的是比当前等级低一级的题目
        elif rank_index == self.rank_index - 1:
            self.progress += 1
            
        # 完成的是比当前等级高的题目
        elif rank_index > self.rank_index:
            difference = rank_index - self.rank_index
            self.progress += 10 * difference * difference
        
        # 如果进度大于100，升级，每减去100进度，升一级    
        while self.progress >= 100:
            self.rank_index += 1
            self.rank = self.RANKS[self.rank_index]
            self.progress -= 100    
        
            # 如果升到8级（最高级），进度被置为0
            if self.rank == 8:
                self.progress = 0
                break
        if self.rank==8:
            self.progress = 0
```

---

### 第三部分

使用Mermaid绘制程序的**类图**

安装VSCode插件：

- Markdown Preview Mermaid Support
- Mermaid Markdown Syntax Highlighting

使用Markdown语法绘制你的程序绘制程序类图（至少一个），Markdown代码如下：

![程序类图](./img/2023-08-08-22-47-53.png)

显示效果如下：

```mermaid
---
title: Animal example
---
classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int sizeInFeet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
```

查看Mermaid类图的语法-->[点击这里](https://mermaid.js.org/syntax/classDiagram.html)

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，包括[实验过程与结果](#实验过程与结果)、[实验考查](#实验考查)和[实验总结](#实验总结)，并将其导出为 **PDF格式** 来提交。

## 实验过程与结果

请将实验过程与结果放在这里，包括：

- [第一部分 Python面向对象编程](#第一部分)
- [第二部分 Codewars Kata挑战](#第二部分)
- [第三部分 使用Mermaid绘制程序流程图](#第三部分)

注意代码需要使用markdown的代码块格式化，例如Git命令行语句应该使用下面的格式：

![Git命令](./img/2023-07-26-22-48.png)

显示效果如下：

```bash
git init
git add .
git status
git commit -m "first commit"
```

如果是Python代码，应该使用下面代码块格式，例如：

![Python代码](./img/2023-07-26-22-52-20.png)

显示效果如下：

```python
def add_binary(a,b):
    return bin(a+b)[2:]
```

代码运行结果的文本可以直接粘贴在这里。

**注意：不要使用截图，Markdown文档转换为Pdf格式后，截图可能会无法显示。**

## 实验考查

请使用自己的语言并使用尽量简短代码示例回答下面的问题，这些问题将在实验检查时用于提问和答辩以及实际的操作。

1. Python的类中__init__方法起什么作用？
答：在Python的类中，`__init__` 方法是一个特殊的方法，用于初始化对象的状态。它会在创建新对象时自动调用，并可用于对对象的属性进行初始化或执行其他必要的操作。
具体来说，`__init__` 方法允许在创建对象时传递参数，并将这些参数用于设置对象的初始状态。可以在 `__init__` 方法内部使用 `self` 参数来引用正在被创建的对象，并使用其属性来存储传递进来的参数值。

下面是一个简单的类及其 `__init__` 方法的示例：

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(person1.name)  # 输出结果为 "Alice"
print(person1.age)  # 输出结果为 25
```
在上述示例中，`Person` 类有一个 `__init__` 方法，该方法接受 `name` 和 `age` 两个参数，并将它们分别赋值给 `self.name` 和 `self.age` 属性。当通过 `Person("Alice", 25)` 创建新的对象时，`__init__` 方法会自动调用，并将参数值传递给相应的属性。最后，我们可以通过访问对象的属性来获取和使用这些初始值。

总结起来，`__init__` 方法在类的实例化过程中起到了初始化对象的作用，对实例的属性进行赋值，使得对象在创建时可以具有初始状态。
<br></br>
2. Python语言中如何继承父类和改写（override）父类的方法。
答：在Python语言中，继承父类和改写父类的方法都非常容易，只需要按照以下两个步骤即可：

①定义子类，并在类定义中指定要继承的父类。这可以通过将父类作为子类定义的元组参数之一来完成，例如：`class SubClass(BaseClass):`。

②在子类中定义方法，并在需要的时候改写父类中的方法。可以使用与父类中同名的方法名来覆盖继承的方法。

下面是一个简单的示例，演示了如何继承父类和改写父类的方法：

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def make_sound(self):
        print("The dog barks.")

my_animal = Animal("Animal")
my_animal.make_sound()  # 输出结果为 "The animal makes a sound."

my_dog = Dog("Fido", "Golden Retriever")
my_dog.make_sound()  # 输出结果为 "The dog barks."
```
在上述示例中，`Animal` 类有一个名为 `make_sound` 的方法，用于输出动物发出的声音。在 `Dog` 类中，我们继承了 `Animal` 类，并添加了一个名为 `breed` 的属性。我们还改写了 `make_sound` 方法，使之输出狗叫的声音。注意，在 `Dog` 类的 `__init__` 方法中，我们使用了 `super` 函数来初始化父类的属性。
最后，我们创建了一个 `Animal` 对象和一个 `Dog` 对象，并分别调用它们的 `make_sound` 方法。可以看到，`Animal` 对象发出了一种默认的声音，而 `Dog` 对象则发出了它自己的声音。

总之，继承和改写父类的方法是Python面向对象编程中非常常用的特性，它们使代码得以更好地组织和复用。
<br></br>
3. Python类有那些特殊的方法？它们的作用是什么？请举三个例子并编写简单的代码说明。
答：在Python中，类有许多特殊的方法，也称为魔法方法或魔术方法，它们以双下划线 `__` 开头和结尾。这些特殊方法在类中定义了许多有用的行为，例如在创建对象时进行初始化、支持算术运算、比较对象等。下面列出了一些常用的特殊方法及其作用：

① `__init__(self, ...)`: 该方法是类被实例化时自动调用的构造函数，它用于初始化对象的状态。在这个方法中，我们可以为对象设置属性和执行其他必要的操作。

②`__str__(self)`: 该方法用于定义对象的字符串表示形式，它会在使用 `print()` 函数打印对象时被自动调用。我们可以在该方法中返回一个字符串，用于描述对象的状态。

③`__eq__(self, other)`: 该方法用于判断两个对象是否相等，当使用 `==` 运算符比较两个对象时，该方法会被自动调用。我们可以在这个方法中定义自己的对象比较方式。

下面是一个简单的示例代码，演示了如何在类中使用这些特殊方法：

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person object - name: {self.name}, age: {self.age}"
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1)  # 输出结果为 "Person object - name: Alice, age: 25"

if person1 == person2:
    print("They are the same person.")
else:
    print("They are different people.")  # 输出结果为 "They are different people."

person3 = Person("Alice", 25)

if person1 == person3:
    print("They are the same person.")  # 输出结果为 "They are the same person."
else:
    print("They are different people.")
```
在上述示例中，我们定义了一个 `Person` 类，并实现了 `__init__`、`__str__` 和 `__eq__` 三个特殊方法。`__init__` 方法用于初始化对象的状态，`__str__` 方法用于设置对象的字符串表现形式，`__eq__` 方法用于自定义对象的比较规则。
接下来，我们创建了三个 `Person` 对象，并使用 `print` 函数打印其中一个对象的字符串表示形式。然后，我们使用 `==` 运算符比较了两个人，打印出它们是否为同一个人的信息。
最后，我们创建了一个名为 `person3` 的新对象，并以相同的名称和年龄对其进行初始化。通过调用 `==` 运算符，我们可以看到它们被认为是相同的人，因为它们拥有相同的名称和年龄。

总之，特殊方法使得Python类拥有了更加灵活的行为和功能，极大地增强了代码的可读性和可维护性。
<br></br>

## 实验总结

总结一下这次实验你学习和使用到的知识，例如：编程工具的使用、数据结构、程序语言的语法、算法、编程技巧、编程思想。

实验中学习，学习中进步，不断汲取经验，累计知识，真正实现实践的锻炼意义。