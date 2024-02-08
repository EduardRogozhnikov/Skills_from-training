# TODO здесь писать код
import functools
from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
      @functools.wraps(func)
      def question_answer() -> None:
            how_are_u = input("kak dela? ")
            my_func = func()
            print("A y menya ne оч! Ладно, держи свою функцию.")
            return my_func
      return question_answer


@how_are_you
def test():
    print("Интересные факты про капибар:\n"
          "1. Они живут группами\n"
          "2. Капибары питаются растениями\n"
          "3. Капибары — сумеречные животные \n"
          "4. У них уникальные вокальные данные \n"
          "5. Они могут весить как человек \n"
          "6. Капибары могут спать в воде \n"
          "7. Капибары — очень социальные животные, которые живут группами по 10 штук. \n"
          "8. В сезон дождей можно встретить группы и до 40 особей, состоящие из одного доминирующего "
          "самца, самок и подчиненных самцов, а также детенышей.")


test()
