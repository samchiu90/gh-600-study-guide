# [Preparing to use custom agents in your organization](https://docs.github.com/api/article/body?pathname=/en/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents)

https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents

Configure the repository that stores custom agents for your organization.

> \[!NOTE]
> Copilot custom agents are in public preview and subject to change.

## Prerequisites

You should understand what Copilot custom agents are and how they work. See [About custom agents](/en/copilot/concepts/agents/cloud-agent/about-custom-agents).

> \[!NOTE]
> If your organization is part of an enterprise, enterprise owners can configure a ruleset that restricts custom agents. Contact your enterprise owners to check whether you can create and manage organization-level custom agents.

## Preparing your organization for custom agents

Organization-level custom agents are stored in the `/agents` directory of your organization's `.github` or `.github-private` repository. Both work the same way and make the custom agents available to all members of the organization, regardless of whether they have access to the repository itself.

For more information on `.github` and `.github-private` repositories, see [Customizing your organization's profile](/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile).

If you don't already have a suitable repository, follow the steps below to create one. These steps describe creating a `.github-private` repository, but you can also create a `.github` repository by naming it `.github` instead.

1. Create your custom agent repository using [GitHub's template repository](https://github.com/docs/custom-agents-template?ref_product=copilot\&ref_type=engagement\&ref_style=text). The template includes a README and the file structure you need.

2. In the **Choose an owner** <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-triangle-down" aria-label="triangle-down" role="img"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg> dropdown menu, choose your organization.

3. Name the repository `.github-private` and write a brief description.

4. In the visibility dropdown menu, click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-lock" aria-label="lock" role="img"><path d="M4 4a4 4 0 0 1 8 0v2h.25c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25v-5.5C2 6.784 2.784 6 3.75 6H4Zm8.25 3.5h-8.5a.25.25 0 0 0-.25.25v5.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25ZM10.5 6V4a2.5 2.5 0 1 0-5 0v2Z"></path></svg> **Private**.
   * Organization members will still be able to use custom agents stored in this repository, regardless of whether they have direct access to the repository itself. Keeping the repository private also avoids conflicts with other features that require `.github-private` to be private, such as the organization member-only profile README.
   * If you want organization members to view and collaborate on the agent profiles directly, consider using a `.github` repository with <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-organization" aria-label="organization" role="img"><path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path></svg> **Internal** visibility. If you are an open source organization and want to share the custom agents publicly, select <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-globe" aria-label="globe" role="img"><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM5.78 8.75a9.64 9.64 0 0 0 1.363 4.177c.255.426.542.832.857 1.215.245-.296.551-.705.857-1.215A9.64 9.64 0 0 0 10.22 8.75Zm4.44-1.5a9.64 9.64 0 0 0-1.363-4.177c-.307-.51-.612-.919-.857-1.215a9.927 9.927 0 0 0-.857 1.215A9.64 9.64 0 0 0 5.78 7.25Zm-5.944 1.5H1.543a6.507 6.507 0 0 0 4.666 5.5c-.123-.181-.24-.365-.352-.552-.715-1.192-1.437-2.874-1.581-4.948Zm-2.733-1.5h2.733c.144-2.074.866-3.756 1.58-4.948.12-.197.237-.381.353-.552a6.507 6.507 0 0 0-4.666 5.5Zm10.181 1.5c-.144 2.074-.866 3.756-1.58 4.948-.12.197-.237.381-.353.552a6.507 6.507 0 0 0 4.666-5.5Zm2.733-1.5a6.507 6.507 0 0 0-4.666-5.5c.123.181.24.365.353.552.714 1.192 1.436 2.874 1.58 4.948Z"></path></svg> **Public** visibility.

5. Click **Create repository**.

6. Update the template README. Include any creation guidelines for custom agents or compliance considerations specific to your organization.

## Next steps

To trial custom agents, see [Testing and releasing custom agents in your organization or enterprise](/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/test-custom-agents).