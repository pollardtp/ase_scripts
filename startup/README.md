# README

Set up ssh key on HPC.

```ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_git -C 'foo@mail.com'```

```cat ~/.ssh/id_rsa_git.pub```

Copy to github.

```git clone git@github.com:pollardtp/foo.git```
