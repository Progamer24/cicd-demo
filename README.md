# CI/CD Demo

A small Python project demonstrating continuous integration and continuous deployment with GitHub Actions and GitHub Pages.

## Project structure

```text
cicd-demo/
├── .github/
│   └── workflows/
│       └── pipeline.yml
├── site/
│   └── index.html
├── app.py
├── test_app.py
└── README.md
```

## Run locally

Make sure Python is installed.

```bash
python app.py
```

This generates `site/index.html`.

Run the tests:

```bash
pip install pytest
pytest
```

## GitHub Pages setup

1. Create a public GitHub repository.
2. Upload or push the project files.
3. Open **Settings → Pages**.
4. Under **Build and deployment**, select **GitHub Actions**.
5. Push a commit to the `main` branch.
6. Open the **Actions** tab and wait for the workflow to finish.
7. Return to **Settings → Pages** and open the deployed site.

## CI/CD flow

The workflow first runs the tests. The deployment job depends on the test job, so deployment only happens when the tests pass.

To demonstrate a failed pipeline, temporarily change:

```python
return a + b
```

to:

```python
return a - b
```

The `test_add` test will fail and the deployment job will not run.

Change it back to `a + b` and push again to restore a successful deployment.

## Terminal commands

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin <GitHub repository URL>
git push -u origin main
```
