from abc import ABC, abstractmethod
from typing import NamedTuple, Tuple, Generator, TYPE_CHECKING, cast, Sequence
import random


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


class SubtractionProblem(Problem):
    def __init__(self, num_a:float, num_b:float) -> None:
        self._num_a = num_a
        self._num_b = num_b

    @property
    def question(self) -> str:
        return f'{self._num_a:g} - {self._num_b:g} = '

    @property
    def answer(self) -> Answers:
        return Answers((self._num_a - self._num_b, ), units=UNITLESS)

    @property
    def question_latex(self) -> str:
        return f'${self._num_a:g} - {self._num_b:g} = $'

    @property
    def answer_latex(self) -> str:
        return f'${self.answer.values[0]:g} {self.answer.units.short_name}$'

    @property
    def solution_latex(self) -> str:
        return f'${self.question}{self.answer}$'


class MultiplicationProblem(Problem):
    def __init__(self, num_a:float, num_b:float) -> None:
        self._num_a = num_a
        self._num_b = num_b

    @property
    def question(self) -> str:
        return f'{self._num_a:g} * {self._num_b:g} = '

    @property
    def answer(self) -> Answers:
        return Answers((self._num_a * self._num_b, ), units=UNITLESS)

    @property
    def question_latex(self) -> str:
        return f'${self._num_a:g} * {self._num_b:g} = $'

    @property
    def answer_latex(self) -> str:
        return f'${self.answer.values[0]:g} {self.answer.units.short_name}$'

    @property
    def solution_latex(self) -> str:
        return f'${self.question}{self.answer}$'

class DivisionProblem(Problem):
    def __init__(self, num_a:float, num_b:float) -> None:
        self._num_a = num_a
        self._num_b = num_b

    @property
    def question(self) -> str:
        return f'{self._num_a:g} / {self._num_b:g} = '

    @property
    def answer(self) -> Answers:
        return Answers((self._num_a / self._num_b, ), units=UNITLESS)

    @property
    def question_latex(self) -> str:
        return f'${self._num_a:g} / {self._num_b:g} = $'

    @property
    def answer_latex(self) -> str:
        return f'${self.answer.values[0]:g} {self.answer.units.short_name}$'

    @property
    def solution_latex(self) -> str:
        return f'${self.question}{self.answer}$'


def binary_operation_problem_generator(decimal_places:int=0, lowest_number:int=0, highest_number:int=10, seed:int=-1, problem_types:Sequence[type] = (AdditionProblem, )) -> Generator[Problem, None, None]:
    if decimal_places < 0:
        raise ValueError('decimal_places must be >= 0')

    for prob_type in problem_types:
        if not issubclass(prob_type, Problem):
            raise ValueError(f'{prob_type} is not a subclass of Problem')

    if seed == -1:
        random.seed()
    else:
        random.seed(seed)

    decimal_factor:int = 10 ** decimal_places

    lowest_rand:int = lowest_number * decimal_factor
    highest_rand:int = highest_number * decimal_factor

    while True:

        num_a:float = random.randint(lowest_rand, highest_rand) / decimal_factor
        num_b:float = random.randint(lowest_rand, highest_rand) / decimal_factor
        problem_type:type = random.choice(problem_types)
        yield cast(Problem, problem_type(num_a, num_b))

    random.seed()





if __name__ == '__main__':

    print('======================')
    print('defalut:')
    for _, prob in zip(range(2), binary_operation_problem_generator()):
        print('======================')
        print(prob.question)
        print(prob.answer)
        print(prob.question_latex)
        print(prob.answer_latex)
        print(prob.solution_latex)

    print('======================')
    print('seeded:')
    for _, prob in zip(range(2), binary_operation_problem_generator(seed=1)):
        print('======================')
        print(prob.question)
        print(prob.answer)
        print(prob.question_latex)
        print(prob.answer_latex)
        print(prob.solution_latex)

    print('======================')
    print('negetive numbers:')
    for _, prob in zip(range(2), binary_operation_problem_generator(lowest_number=-10)):
        print('======================')
        print(prob.question)
        print(prob.answer)
        print(prob.question_latex)
        print(prob.answer_latex)
        print(prob.solution_latex)

    print('======================')
    print('decimals:')
    for _, prob in zip(range(2), binary_operation_problem_generator(decimal_places=2)):
        print('======================')
        print(prob.question)
        print(prob.answer)
        print(prob.question_latex)
        print(prob.answer_latex)
        print(prob.solution_latex)

    print('======================')
    print('addition, subtraction, multiplication and division:')
    for _, prob in zip(range(5), binary_operation_problem_generator(problem_types =(AdditionProblem, SubtractionProblem, MultiplicationProblem, DivisionProblem))):
        print('======================')
        print(type(prob))
        print(prob.question)
        print(prob.answer)
        print(prob.question_latex)
        print(prob.answer_latex)
        print(prob.solution_latex)

    #print('error:')
    #for _, prob in zip(range(2), binary_operation_problem_generator(decimal_places=-1)):
    #    print('======================')
    #    print(prob.question)
    #    print(prob.answer)
    #    print(prob.question_latex)
    #    print(prob.answer_latex)
    #    print(prob.solution_latex)

    #for _, prob in zip(range(5), binary_operation_problem_generator(problem_types =(AdditionProblem, int))):
    #    print('======================')
    #    print(type(prob))
    #    print(prob.question)
    #    print(prob.answer)
    #    print(prob.question_latex)
    #    print(prob.answer_latex)
    #    print(prob.solution_latex)
