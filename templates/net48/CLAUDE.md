# .NET Framework 4.8 project guidance

- Identify the solution, startup project, deployment host and selected MSBuild configuration.
- Confirm the matching Developer Pack on Windows. Check each project for packages.config or PackageReference and restore with the repository’s configured tooling.
- Preserve public HTTP and SOAP contracts, SQL result grain, form designer files, and existing package and binding settings.
- Keep fixture data synthetic and avoid storing credentials in repository files.
- Build with Visual Studio MSBuild and run the repository's configured Windows test runner. Record the executed commands and their outcomes.
