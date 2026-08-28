# Contributing

Thanks for your interest in improving this project.

## How to contribute

1. Fork the repository and create a feature branch.
2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Make your changes and keep them focused.
4. Run the relevant checks before opening a pull request:

```bash
python manage.py check
python manage.py test
```

5. Open a pull request with a clear description of the change.

## Code style

- Follow the existing Django project structure and naming conventions.
- Keep commits small and easy to review.
- Prefer readable, maintainable code over clever shortcuts.

## Reporting bugs

Please open an issue with:

- a clear description of the problem
- steps to reproduce it
- expected vs actual behavior
- relevant environment details

## Questions

If you have questions about the project or a contribution idea, start by opening a discussion or issue in the repository.
