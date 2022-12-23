# 4 Digit MWC Media Centre Articles

This is a documentation for 4 Digit MWC Media Centre Workflow via Github.

## Main tools

### Article Writing

For Article Writing, we will use **markdown (.md)** for writing articles. This format is closest to discord message format and easy to use. There are so many applications which support this.

#### Recommended Applications

- [Notion](https://www.notion.so/)
    - [Documentation](#notion)
- [Visual Studio Code](https://code.visualstudio.com/)
    - [Documentation](#visual-studio-code)
- [Discord](https://discord.com/) if you are a psychopath

#### Markdown Tutorial Resources

- [Markdown tutorial (markdownguide.org)](https://www.markdownguide.org/)
- [Cheat Sheet (markdownguide.org)](https://www.markdownguide.org/cheat-sheet/)

#### Notion

[**Notion**](https://www.notion.so/) is a cloud based planning and notetaking application. It has a feature for Markdown Importing and Exporting.

To create an article, start by creating an account on Notion, then it will bring you to a dashboard. Select **New Page**.

![](https://cdn.discordapp.com/attachments/546525809440194560/1010563019476045894/unknown.png)

Create a title of a new page. (Article Name)

![](https://cdn.discordapp.com/attachments/546525809440194560/1010563537082519732/unknown.png)

Then Press Enter. After that the page is ready for writing a story. You can learn more on how to use Notion [here](https://www.notion.so/help/category/new-to-notion).

In order to export a Notion Article to a markdown file, select **ellipsis (...)** then select **Export**.

![](https://cdn.discordapp.com/attachments/546525809440194560/1010565787506978957/unknown.png)

Make sure the settings are the same as following:

![](https://cdn.discordapp.com/attachments/546525809440194560/1010566089018703943/unknown.png)

Then **Export**.

Notion will deliver a `.zip` file, extract them and rename a markdown file. [Upload it to Github](#creating-file--uploading-file) and [Request for reviews](#pull-requests) in order to publish an article.

#### Visual Studio Code

To start with **Visual Studio Code**, create a folder for articles then select **File** then **Open Folder**.

![](https://cdn.discordapp.com/attachments/546525809440194560/1010568109507231755/unknown.png)

Choose a folder which is reserved for articles. Then create a file by right clicking at the left space than select **New File**.

![](https://cdn.discordapp.com/attachments/546525809440194560/1010568558750748722/unknown.png)

Name a file with the extension `.md`.

![](https://cdn.discordapp.com/attachments/546525809440194560/1010568899051409468/unknown.png)

Following [Markdown Tutorials](#markdown-tutorial-resources) to write the articles. To observe a preview parallel with writing markdown, select this:

![](https://cdn.discordapp.com/attachments/546525809440194560/1010569375952146432/unknown.png)

To export the markdown, open a directory where the articles are stored then [Upload the desired markdown file to Github](#creating-file--uploading-file) and [Request for reviews](#pull-requests) in order to publish an article.

## Workflow

### Github

In order to get access to **Media Centre** and **4dm Repositories** in general, create a [Github](https://github.com/) account, then contact me (HowToPlayLN) with the Github profile link in order to be added into a [4digitmwc Organization](https://github.com/4digitmwc).

### Create Branch

You will see many repositories, but the one we're going to use to write the articles is [media-centre-articles](https://github.com/4digitmwc/media-centre-articles).

Create a separate branch by selecting at the branch icon. The branch name must be in format `yourname/<updates>` (example below).

![](https://cdn.discordapp.com/attachments/546525809440194560/1009835163632545915/unknown.png)

Then select "Create branch".

### Creating File / Uploading File

After finishing your Article Markdown, go to the folder (stories/interviews/opinions) and upload the file based on category you wrote.

For example, if you create a new story, you upload the story by selecting `stories` folder.

![](https://cdn.discordapp.com/attachments/546525809440194560/1009837843469844542/unknown.png)

Then select **Add File** and then **Upload Files** in the dropdown menu.

![](https://cdn.discordapp.com/attachments/546525809440194560/1009838181480415313/unknown.png)

Then you drop your markdown file or choose from your directory and write a commit message.

![](https://cdn.discordapp.com/attachments/546525809440194560/1009838767114309693/unknown.png)

Then select **Commit Changes**.

### Pull Requests

After you added new articles or update them, you need to do **Pull Request** for articles to be reviewed. You start by selecting **Pull Requests**.

![](https://cdn.discordapp.com/attachments/546525809440194560/1009839539717677216/unknown.png)

Then, select **New Pull Request**, then change the `compare:` to your branch (below for example).

![](https://cdn.discordapp.com/attachments/546525809440194560/1009839898469089321/unknown.png)

Select **Create Pull Request** and it will bring you to this page.

![](https://cdn.discordapp.com/attachments/546525809440194560/1009840139146641478/unknown.png)

Edit title and description of your Pull Request as you like, then **Create Pull Request**.

Next, **Request Reviews** by selecting **Conversation** and then select **Reviewers** according to a following image.

![](https://cdn.discordapp.com/attachments/546525809440194560/1010558240528007208/unknown.png)

You can Request Reviews by selecting Github usernames of members you want to assign for reviews.

Another way is to send the **Pull Request URL** to 4dm Media Centre Group Chat and wait for reviews from members. 

### Reviews

In order to review a Pull Request from a different author, you redirect into a Pull Request URL and go to **Files changed**, select **Review Changes** and add your comments.

![](https://cdn.discordapp.com/attachments/546525809440194560/1009842057034084352/unknown.png)

If you think this article still needs changes, select **Comment** or **Request Changes**. Or if you think it's ready-to-go select **Approve**.

Normally, it's like ranking a map, you need two BNs to approve your map in order to be ranked. This one you need at least two contributors to Approve your pull request in order to merge into the main branch (for a private repository) and 1 more approval from a contributor in a public repository.

**Additional Information:** All the pushes/updates/reviews will be done in the private repository, then they will be published into a public repository after the week has come.
