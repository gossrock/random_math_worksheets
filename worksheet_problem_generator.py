from abc import ABC, abstractmethod
from typing import NamedTuple, Tuple, Generator, TYPE_CHECKING
import random

if TYPE_CHECKING:
    def randint(a:int, b:int) -> int: ...


class Units(NamedTuple):
    short_name: str
    long_name: str
    latex: str

class Answers(NamedTuple):
    values:Tuple[float]
    units:Units

    def __str__(self) -> str:
        return_str = ''
        for i, answer in enumerate(self.values):
            if i != 0:
                return_str += ', '
            return_str += f'{answer:g}{self.units.short_name}'
        return return_str



UNITLESS = Units('','','')
#Time
SECONDS = Units(short_name='s', long_name='seconds', latex='s')

#Length
METERS = Units(short_name='m',long_name='meters', latex='m')

#Area
SQUARE_METERS = Units(short_name='m^2',long_name='square meters', latex='$m^2$')

#Volume

#Speed

#Acceleration


class Problem(ABC):
    @property
    @abstractmethod
    def question(self) -> str: ...

    @property
    @abstractmethod
    def answer(self) -> Answers: ...

    @property
    @abstractmethod
    def question_latex(self) -> str: ...

    @property
    @abstractmethod
    def answer_latex(self) -> str: ...

    @property
    @abstractmethod
    def solution_latex(self) -> str: ...


class AdditionProblem(Problem):
    def __init__(self, num_a:float, num_b:float) -> None:
        self._num_a = num_a
        self._num_b = num_b

    @property
    def question(self) -> str:
        return f'{self._num_a:g} + {self._num_b:g} = '

    @property
    def answer(self) -> Answers:
        return Answers((self._num_a + self._num_b, ), units=UNITLESS)

    @property
    def question_latex(self) -> str:
        return f'${self._num_a:g} + {self._num_b:g} = $'

    @property
    def answer_latex(self) -> str:
        return f'${self.answer.values[0]:g} {self.answer.units.short_name}$'

    @property
    def solution_latex(self) -> str:
        return f'${self.question}{self.answer}$'


def addition_problem_generator(decimal_places:int=0, lowest_number:int=0, highest_number:int=10, seed:int=-1) -> Generator[AdditionProblem, None, None]:
    if seed == -1:
        random.seed()
    else:
        random.seed(seed)

    lowest_rand = lowest_number * (10**decimal_places)
    highest_rand = highest_number * 10**decimal_places

    while True:

        num_a = random.randint(lowest_rand, highest_rand) / (10**decimal_places)
        num_b = random.randint(lowest_rand, highest_rand) / (10**decimal_places)
        yield AdditionProblem(num_a, num_b)


    random.seed()





if __name__ == '__main__':

    print('======================')
    print('defalut:')
    for _, prob in zip(range(2), addition_problem_generator()):
        print('======================')
        print(prob.question)
        print(prob.answer)
        print(prob.question_latex)
        print(prob.answer_latex)
        print(prob.solution_latex)

        print('======================')
        print('seeded:')
        for _, prob in zip(range(2), addition_problem_generator(seed=1)):
            print('======================')
            print(prob.question)
            print(prob.answer)
            print(prob.question_latex)
            print(prob.answer_latex)
            print(prob.solution_latex)

        print('======================')
        print('negetive numbers:')
        for _, prob in zip(range(2), addition_problem_generator(lowest_number=-10)):
            print('======================')
            print(prob.question)
            print(prob.answer)
            print(prob.question_latex)
            print(prob.answer_latex)
            print(prob.solution_latex)
