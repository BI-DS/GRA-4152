import argparse
from sklearn.linear_model import LogisticRegression

def my_logistic_regression():
    parser = argparse.ArgumentParser(description='My logistic regression',
                                     epilog='you can go to: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html')
    
    parser.add_argument('--penalty', choices=["option1", "option2", "option3", "option4"], help='the penalty argument')
    parser.add_argument('--fit_intercept', action="store_true", help='specify fit_intercept as True by default')
    parser.add_argument('--max_iter', type=int, default=10, help='max_iter argument, default: 10')
    parser.add_argument('--tol', type=int, default=1, help='tol argument, default: 1')

    args = parser.parse_args()

    clf = LogisticRegression(penalty=args.penalty,
                             fit_intercept=args.fit_intercept,
                             max_iter=args.max_iter,
                             tol=args.tol
                             )

    print(args)

if __name__ == "__main__":
    my_logistic_regression()
