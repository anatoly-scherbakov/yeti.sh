---
$id: jira-cli-tools
title: Comparison of CLI tools for JIRA
date: 2021-10-13
description: If you have to use Atlassian JIRA a lot, you very quickly grow tired of the multitude of routine operations in the system's UI. Wishing to improve your productivity you start looking for a CLI tool.
---

{{ page.meta.description }}

This page is an overview of several CLI tools to manage issues in JIRA that I had a chance to review. This page was only written after I spent time to write my own rudimentary tool in Python and to use it for a while, — only to find out later that there are a few much more mature tools which I should have been using instead in the first place. That's the importance of doing proper research: that might save you a lot of effort and precious time. Better later then never, right?

{% set products = query(
'''
SELECT * WHERE {
    ?product
        :token-in-env ?evaluation ;
        octa:title ?title ;
        :language ?language .
    ?evaluation
        :is ?value ;
        :because ?source ;
        rdfs:comment ?comment .
}
'''
) %}

<table>
    <thead>
        <tr>
            <th>Product</th>
            <th>Language</th>
            <th>
                <a href="criteria/auth/" target="_blank">
                    Auth token in env
                </a>
            </th>
            <th>
                Supports <code>fixVersions</code> field
            </th>
            <th>CLI options → JQL query</th>
        </tr>
    </thead>
    <tbody>
        {% for product in products %}
            <tr>
                <td>
                    <a href="{{ product.product }}">{{ product.title }}</a>                    
                </td>
                <td>{{ product.language }}</td>
                <td>
                    <a href="{{ source }}" title="{{ product.comment }}" target="_blank">
                        {% if product.value %}✔️{% else %}❌{% endif %}
                    </a>
                </td>
                <td>
                    {% set fix_versions = query(
                        '''
                        SELECT * WHERE {
                            ?item :fix-versions-support ?ref .
                            
                            ?ref
                                :is ?value ;
                                rdfs:comment ?comment .
                        }
                        ''',
                        item=product.product
                    ).first %}

                    {% if fix_versions %}
                        <a href="{{ fix_versions.item }}" title="{{ fix_versions.comment }}" target="_blank">
                            {% if fix_versions.value %}✔️{% else %}❌{% endif %}
                        </a>
                    {% endif %}
                </td>
                <td>
                    {% set jql_builder = query(
                        '''
                        SELECT * WHERE {
                            ?item :jql_builder ?ref .
                            
                            ?ref :is ?value .

                            OPTIONAL {
                                ?ref rdfs:comment ?comment .
                            }
                        }
                        ''',
                        item=product.product
                    ).first %}

                    {% if jql_builder %}
                        <a href="{{ jql_builder.item }}" title="{{ jql_builder.comment }}" target="_blank">
                            {% if jql_builder.value %}✔️{% else %}❌{% endif %}
                        </a>
                    {% endif %}
                </td>
            </tr>
        {% endfor %}
    </tbody>
</table>


!!! warning "Unmaintained"
    I am no longer using JIRA, and therefore the page hadn't been updated since the moment of original publication.
