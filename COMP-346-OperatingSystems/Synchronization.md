# Synchronization
<hr>

==Bad things can happen when two different threads share the same memory==
Already saw the famous basic example of [Producer Consumer Problem](Producer_Consumer_Problem.md).
Here's another example (this is called [Race condition](Race_condirion.md))
```java
1    public boolean withdraw(long amount) {
2       if (amount <= balance) {
3          long newBalance = balance – amount;
4          balance = newBalance;
5          return true;
6       } else {
7          return false;
8       }
9    }
```

Consider the following sequence of execution with [Thread](Thread.md) A and B:
1.  balance is 1500
2.  Thread `A` calls `acct.withdraw(1000)`
3.  Thread `A` runs line 2, condition is `true`
4.  Thread `A` runs line 3, computes `newBalance` as `500`
5.  `JVM` Scheduler yanks thread `A` and replaces it with thread `B`
6.  Thread `B` calls `acct.withdraw(1000)` on the same account (acct)
7.  Thread `B` runs line 2, condition is true (balance is still 1500)
8.  Thread `B` runs line 3, `newBalance` as 500
9.  Thread `B` runs line 4, assigns `balance` `500`
10.  Thread `B` runs line 5, returns `true`
11.  JVM Scheduler yanks thread B and replaces it with thread `A`
12.  Thread `A` runs line `4`, assigns balance `500`!
13.  Thread `A` runs line `5`, returns `true`!

In this Race condition example, the `withdraw()` method is not *thread-safe.*


Just because you carefully synchronize methods, that doesn't mean bad things cannot happen in a multi-threaded environment! Consider this sequence:

-   Thread A gets lock on object 1
-   Thread B gets lock on object 2
-   Thread A requests lock on object 2 and is blocked because B has it
-   Thread B requests lock on object 1 and is blocked because A has it!

Neither thread can continue, locked in a "deadly embrace"! Each is waiting for a resource that the other has an exclusive lock on.