# Developer Certificate of Origin (DCO)

## Version 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I have the right to submit it under the open source license indicated in the file; or

(b) The contribution is based upon previous work that, to the best of my knowledge, is covered under an appropriate open source license and I have the right under that license to submit that work with modifications, whether created in whole or in part by me, under the same open source license (unless I am permitted to submit under a different license), as indicated in the file; or

(c) The contribution was provided directly to me by some other person who certified (a), (b) or (c) and I have not modified it.

(d) I understand and agree that this project and the contribution are public and that a record of the contribution (including all personal information I submit with it, including my sign-off) is maintained indefinitely and may be redistributed consistent with this project or the open source license(s) involved.

## How to Sign Off

To sign off on a commit, simply add the following line at the end of your commit message:

```
Signed-off-by: Your Name <your.email@example.com>
```

You can add this automatically to your commits by using the `-s` or `--signoff` flag with your git commit command:

```bash
git commit -s -m "Your commit message"
```

Git will automatically add a `Signed-off-by` line with your name and email as configured in your git settings.

### Configuring Git

Make sure your git user name and email are configured correctly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Why DCO?

The DCO is a lightweight mechanism to certify that you wrote or otherwise have the right to submit the code you are contributing to the project. It helps ensure that the project can legally accept and distribute your contributions.

## Additional Resources

- [Full DCO Text](https://developercertificate.org/)
- [GitHub's DCO App](https://github.com/apps/dco)
- [Understanding the DCO](https://wiki.linuxfoundation.org/dco)
